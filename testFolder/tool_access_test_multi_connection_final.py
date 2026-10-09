"""Smoke-test the authenticated P6 MCP tools in one run.

Environment variables:
    MCP_URL                 Optional. Defaults to http://127.0.0.1:8002/mcp
    AISIDEKICK_MCP_API_KEY  Required. API key for the MCP/Django account.
    P6_CONNECTION_ID        Optional. Defaults to 2.

The script deliberately does NOT call the legacy credential tools
(set_p6_credentials / get_p6_credentials_status). The migrated tools obtain
credentials from the saved P6Connection selected by connection_id.

Create tools are tested with an empty JSON array. They should return a
validation response without changing P6 data. This is intentional: this file
is a smoke test, not a data-creation test.
"""

import asyncio
import json
import os
from typing import Any

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

MCP_URL = os.getenv("MCP_URL", "http://127.0.0.1:8002/mcp")
API_KEY = os.getenv("AISIDEKICK_MCP_API_KEY", "").strip()
CONNECTION_ID = int(os.getenv("P6_CONNECTION_ID", "2"))

READ_FIELDS = "ObjectId,Name"

READ_TOOLS = {
    "get_activities_from_p6": {
        "fields": "ObjectId,Name,ProjectObjectId",
        "filter_condition": "",
        "order_by": "",
    },
    "get_eps_from_p6": {
        "fields": READ_FIELDS,
        "filter_condition": "",
        "order_by": "",
    },
    "get_resources_from_p6": {
        "fields": READ_FIELDS,
        "filter_condition": "",
        "order_by": "",
    },
    "get_resource_assignments_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_user_obs_from_p6": {
        "fields": "OBSObjectId,OBSName",
        "filter_condition": "",
        "order_by": "",
    },
    "get_calendars_from_p6": {
        "fields": READ_FIELDS,
        "filter_condition": "",
        "order_by": "",
    },
    "get_currencies_from_p6": {
        "fields": READ_FIELDS,
        "filter_condition": "",
        "order_by": "",
    },

    "get_cbss_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },
}

CREATE_TOOLS = {
    "create_eps_in_p6": "eps_items_json",
    "create_resources_in_p6": "resource_items_json",
    "create_user_obs_in_p6": "user_obs_items_json",
    "create_projects_in_p6": "project_items_json",
    "create_wbs_in_p6": "wbs_items_json",
    "create_activities_in_p6": "activity_items_json",
    "create_resource_assignments_in_p6": "resource_assignment_items_json",
    "create_resource_curves_in_p6": "resource_curve_items_json",
    "create_risks_in_p6": "risk_items_json",
    "create_activity_notes_in_p6": "activity_note_items_json",
    "create_activity_steps_in_p6": "activity_step_items_json",
    "create_calendars_in_p6": "calendar_items_json",
    "create_currencies_in_p6": "currency_items_json",
}

MIGRATED_TOOLS = {
    "get_project_from_p6",
    *READ_TOOLS.keys(),
    "export_project_from_p6",
    "export_projects_from_p6",
    *CREATE_TOOLS.keys(),
    "clear_p6_session",
}


def result_text(result: Any) -> str:
    """Extract readable text from an MCP CallToolResult."""
    chunks: list[str] = []
    for item in getattr(result, "content", []) or []:
        text = getattr(item, "text", None)
        if text:
            chunks.append(text)
        else:
            chunks.append(str(item))
    return "\n".join(chunks) if chunks else str(result)


def result_json(result: Any) -> dict[str, Any] | None:
    text = result_text(result).strip()
    if not text:
        return None
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        return None


def print_result(label: str, status: str, detail: str = "") -> None:
    suffix = f" | {detail}" if detail else ""
    print(f"{status:<20} | {label}{suffix}")


async def call_tool(session: ClientSession, name: str, args: dict[str, Any]) -> Any:
    return await session.call_tool(name, args)


async def run() -> None:
    if not API_KEY:
        raise SystemExit(
            "AISIDEKICK_MCP_API_KEY is not set. "
            "Set it before running this test."
        )

    print("\nP6 MCP MULTI-CONNECTION SMOKE TEST")
    print(f"MCP URL       : {MCP_URL}")
    print(f"Connection ID : {CONNECTION_ID}")
    print("-" * 80)

    async with streamablehttp_client(
        MCP_URL,
        headers={"X-API-Key": API_KEY},
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            listed = await session.list_tools()
            available = {tool.name: tool for tool in listed.tools}

            print(f"Server tools discovered: {len(available)}")

            missing = sorted(MIGRATED_TOOLS - set(available))
            if missing:
                print_result("tool discovery", "FAIL", f"Missing: {', '.join(missing)}")
                raise SystemExit(1)

            # Verify the migrated tools actually expose connection_id.
            schema_failures = []
            for name in sorted(MIGRATED_TOOLS):
                tool = available[name]
                schema = getattr(tool, "inputSchema", {}) or {}
                properties = schema.get("properties", {})
                if name != "clear_p6_session" and "connection_id" not in properties:
                    schema_failures.append(name)
                if name == "clear_p6_session" and "connection_id" not in properties:
                    schema_failures.append(name)

            if schema_failures:
                print_result(
                    "MCP schema",
                    "FAIL",
                    f"connection_id missing from: {', '.join(sorted(schema_failures))}",
                )
                raise SystemExit(1)

            print_result("MCP schema", "PASS", "Migrated tools expose connection_id")

            # ------------------------------------------------------------------
            # 1. PROJECTS - also supplies a real project ObjectId for exports.
            # ------------------------------------------------------------------
            project_args = {
                "connection_id": CONNECTION_ID,
                "project_filter": "",
            }
            try:
                result = await call_tool(session, "get_project_from_p6", project_args)
                data = result_json(result)
                if data and data.get("success"):
                    projects = data.get("projects") or []
                    project_id = None
                    if projects and isinstance(projects[0], dict):
                        project_id = projects[0].get("ObjectId")
                    print_result(
                        "get_project_from_p6",
                        "PASS",
                        f"count={data.get('count')}, first_project_object_id={project_id}",
                    )
                else:
                    print_result("get_project_from_p6", "FAIL", result_text(result))
                    return
            except Exception as exc:
                print_result("get_project_from_p6", "ERROR", str(exc))
                return

            # ------------------------------------------------------------------
            # 2. READ tools
            # ------------------------------------------------------------------
            for name, tool_args in READ_TOOLS.items():
                args = {"connection_id": CONNECTION_ID, **tool_args}
                try:
                    result = await call_tool(session, name, args)
                    data = result_json(result)
                    if data and data.get("success"):
                        print_result(name, "PASS", f"count={data.get('count')}")
                    else:
                        print_result(name, "FAIL", result_text(result))
                except Exception as exc:
                    print_result(name, "ERROR", str(exc))

            # ------------------------------------------------------------------
            # 3. EXPORT tools
            # ------------------------------------------------------------------
            if project_id is not None:
                export_args = {
                    "connection_id": CONNECTION_ID,
                    "project_object_id": int(project_id),
                }
                try:
                    result = await call_tool(session, "export_project_from_p6", export_args)
                    data = result_json(result)
                    if data and data.get("success"):
                        print_result("export_project_from_p6", "PASS")
                    else:
                        print_result("export_project_from_p6", "FAIL", result_text(result))
                except Exception as exc:
                    print_result("export_project_from_p6", "ERROR", str(exc))

                export_many_args = {
                    "connection_id": CONNECTION_ID,
                    "project_object_ids": str(project_id),
                }
                try:
                    result = await call_tool(session, "export_projects_from_p6", export_many_args)
                    data = result_json(result)
                    if data and data.get("success"):
                        print_result("export_projects_from_p6", "PASS")
                    else:
                        print_result("export_projects_from_p6", "FAIL", result_text(result))
                except Exception as exc:
                    print_result("export_projects_from_p6", "ERROR", str(exc))
            else:
                print_result("export tools", "SKIP", "No project ObjectId was returned")

            # ------------------------------------------------------------------
            # 4. CREATE tools - safe validation-only calls.
            # ------------------------------------------------------------------
            for name, json_arg_name in CREATE_TOOLS.items():
                args = {
                    "connection_id": CONNECTION_ID,
                    json_arg_name: "[]",
                }
                try:
                    result = await call_tool(session, name, args)
                    data = result_json(result)
                    text = result_text(result)
                    if data and data.get("success"):
                        # An empty-array test unexpectedly succeeded. Flag it so
                        # we know it did not exercise the intended validation path.
                        print_result(name, "WARN", "empty payload was accepted")
                    elif data is not None and data.get("success") is False:
                        print_result(name, "EXPECTED", "validation rejected empty payload")
                    elif "validation" in text.lower() or "at least one" in text.lower():
                        print_result(name, "EXPECTED", "validation response")
                    else:
                        print_result(name, "CHECK", text)
                except Exception as exc:
                    print_result(name, "ERROR", str(exc))

            # ------------------------------------------------------------------
            # 5. Clear only this connection's cached session.
            # ------------------------------------------------------------------
            try:
                result = await call_tool(
                    session,
                    "clear_p6_session",
                    {"connection_id": CONNECTION_ID},
                )
                data = result_json(result)
                if data and data.get("success"):
                    print_result("clear_p6_session", "PASS", data.get("message", ""))
                else:
                    print_result("clear_p6_session", "FAIL", result_text(result))
            except Exception as exc:
                print_result("clear_p6_session", "ERROR", str(exc))

            # Re-login after clearing to prove the connection manager can rebuild
            # the session from Django/P6 for the same connection_id.
            try:
                result = await call_tool(session, "get_project_from_p6", project_args)
                data = result_json(result)
                if data and data.get("success"):
                    print_result("get_project_from_p6 (re-login)", "PASS")
                else:
                    print_result("get_project_from_p6 (re-login)", "FAIL", result_text(result))
            except Exception as exc:
                print_result("get_project_from_p6 (re-login)", "ERROR", str(exc))

        print("-" * 80)
        print("Smoke test completed.")
        print("EXPECTED = safe validation response; no P6 data was created by those calls.")


if __name__ == "__main__":
    asyncio.run(run())
