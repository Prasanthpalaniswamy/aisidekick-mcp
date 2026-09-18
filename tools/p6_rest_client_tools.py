import base64
import json
import sys
from pathlib import Path
from typing import Any

import requests

from mcp.server.fastmcp import Context, FastMCP

from tools.session_store import P6_SESSIONS, get_session_key


# CLIENT_PACKAGE_ROOT = Path(__file__).resolve().parent/ "rest-api-for-oracle-primavera-p6-client"
# if str(CLIENT_PACKAGE_ROOT) not in sys.path:
#     sys.path.insert(0, str(CLIENT_PACKAGE_ROOT))
from pathlib import Path
import sys


CLIENT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    / "rest-api-for-oracle-primavera-p6-client"
)

print("CLIENT_ROOT =", CLIENT_ROOT)

if str(CLIENT_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(CLIENT_ROOT)
    )
from rest_api_for_oracle_primavera_p6_client import Client  # noqa: E402
from rest_api_for_oracle_primavera_p6_client.api.activity import get_activities  # noqa: E402
from rest_api_for_oracle_primavera_p6_client.api.project import get_project  # noqa: E402

# print("TOOLS_ROOT =", TOOLS_ROOT)
# print("sys.path =", sys.path[:3])

REQUEST_TIMEOUT_SECONDS = 30


def _resolve_session(ctx: Context) -> dict[str, Any]:
    return P6_SESSIONS.get(get_session_key(ctx), {})


def _resolve_rest_client(ctx: Context, base_url: str = "", verify_ssl: bool = True) -> tuple[Client, str | None]:
    """Build a client using session-stored base_url first, then explicit input."""
    session = _resolve_session(ctx)
    resolved_base_url = base_url or session.get("base_url")
    if not resolved_base_url:
        raise ValueError("Missing base_url. Set P6 credentials first or pass base_url explicitly.")

    client = Client(base_url=resolved_base_url.rstrip("/"), verify_ssl=verify_ssl)
    auth_token = session.get("auth_token")
    if not auth_token:
        username = session.get("username")
        password = session.get("password")
        if username and password:
            auth_token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    return client, auth_token


def _normalize_result_items(result: list | None) -> list[dict] | dict:
    if result is None:
        return {"success": False, "error": "No data returned from endpoint."}
    return [item.to_dict() if hasattr(item, "to_dict") else item for item in result]


def _with_auth_token(auth_token: str | None) -> dict:
    return {"auth_token": auth_token} if auth_token else {}


def _direct_rest_get_notebook_topics(
    ctx: Context,
    fields: str,
    filter_condition: str = "",
    order_by: str = "",
    base_url: str = "",
) -> list[dict] | dict:
    try:
        resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
        params = {"Fields": fields}
        if filter_condition:
            params["Filter"] = filter_condition
        if order_by:
            params["OrderBy"] = order_by

        response = requests.get(
            f"{resolved_base_url}/notebookTopic",
            headers={"AuthToken": auth_token},
            cookies=cookies,
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
        return payload if isinstance(payload, list) else {"success": True, "notebook_topics": payload}
    except requests.RequestException as exc:
        return {"success": False, "error": f"Direct notebook topic fetch failed: {exc}"}
    except ValueError as exc:
        return {"success": False, "error": f"Invalid notebook topic response JSON: {exc}"}


def _direct_rest_mutate_notebook_topics(
    ctx: Context,
    method: str,
    notebook_topics_json: str | None = None,
    object_id: str | None = None,
    base_url: str = "",
) -> dict:
    try:
        resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
        headers = {"AuthToken": auth_token}
        kwargs: dict[str, Any] = {
            "headers": headers,
            "cookies": cookies,
            "timeout": REQUEST_TIMEOUT_SECONDS,
        }

        if method in {"POST", "PUT"}:
            if not notebook_topics_json:
                raise ValueError("notebook_topics_json is required for create/update operations.")
            payload = json.loads(notebook_topics_json)
            if not isinstance(payload, list) or not payload:
                raise ValueError("notebook_topics_json must be a non-empty JSON array.")
            headers["Content-Type"] = "application/json"
            kwargs["json"] = payload
        elif method == "DELETE":
            if not object_id:
                raise ValueError("object_id is required for delete operations.")
            kwargs["params"] = {"ObjectId": object_id}

        response = requests.request(method, f"{resolved_base_url}/notebookTopic", **kwargs)
        response.raise_for_status()

        try:
            parsed = response.json()
        except ValueError:
            parsed = response.text

        return {
            "success": True,
            "status_code": response.status_code,
            "result": parsed,
        }
    except Exception as exc:
        return {"success": False, "error": f"Direct notebook topic {method.lower()} failed: {exc}"}


def _resolve_direct_auth(ctx: Context, base_url: str = "") -> tuple[str, str, requests.cookies.RequestsCookieJar]:
    session = _resolve_session(ctx)
    resolved_base_url = (base_url or session.get("base_url") or "").rstrip("/")
    username = session.get("username")
    password = session.get("password")
    database_name = session.get("database_name")

    missing = [
        key
        for key, value in {
            "base_url": resolved_base_url,
            "username": username,
            "password": password,
            "database_name": database_name,
        }.items()
        if not value
    ]
    if missing:
        raise ValueError(f"Missing required P6 session values for direct relationship REST call: {', '.join(missing)}")

    auth_token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    login_response = requests.post(
        f"{resolved_base_url}/login",
        headers={"AuthToken": auth_token},
        params={"DatabaseName": database_name},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    login_response.raise_for_status()
    return resolved_base_url, auth_token, login_response.cookies


def _direct_rest_get_relationships(
    ctx: Context,
    fields: str,
    filter_condition: str = "",
    order_by: str = "",
    base_url: str = "",
) -> list[dict] | dict:
    try:
        resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
        params = {"Fields": fields}
        if filter_condition:
            params["Filter"] = filter_condition
        if order_by:
            params["OrderBy"] = order_by

        response = requests.get(
            f"{resolved_base_url}/relationship",
            headers={"AuthToken": auth_token},
            cookies=cookies,
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        payload = response.json()
        return payload if isinstance(payload, list) else {"success": True, "relationships": payload}
    except requests.RequestException as exc:
        return {"success": False, "error": f"Direct relationship fetch failed: {exc}"}
    except ValueError as exc:
        return {"success": False, "error": f"Invalid relationship response JSON: {exc}"}


def _direct_rest_mutate_relationships(
    ctx: Context,
    method: str,
    relationships_json: str | None = None,
    object_id: str | None = None,
    base_url: str = "",
) -> dict:
    try:
        resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
        headers = {"AuthToken": auth_token}
        kwargs: dict[str, Any] = {
            "headers": headers,
            "cookies": cookies,
            "timeout": REQUEST_TIMEOUT_SECONDS,
        }

        if method in {"POST", "PUT"}:
            if not relationships_json:
                raise ValueError("relationships_json is required for create/update operations.")
            payload = json.loads(relationships_json)
            if not isinstance(payload, list) or not payload:
                raise ValueError("relationships_json must be a non-empty JSON array.")
            headers["Content-Type"] = "application/json"
            kwargs["json"] = payload
        elif method == "DELETE":
            if not object_id:
                raise ValueError("object_id is required for delete operations.")
            kwargs["params"] = {"ObjectId": object_id}

        response = requests.request(method, f"{resolved_base_url}/relationship", **kwargs)
        response.raise_for_status()

        try:
            parsed = response.json()
        except ValueError:
            parsed = response.text

        return {
            "success": True,
            "status_code": response.status_code,
            "result": parsed,
        }
    except Exception as exc:
        return {"success": False, "error": f"Direct relationship {method.lower()} failed: {exc}"}


def register_rest_client_tools(mcp: FastMCP) -> None:
    """Register wrapper tools backed by the generated Primavera REST client."""

    @mcp.tool()
    def rest_client_get_projects(
        ctx: Context,
        fields: str = "Name,ObjectId,WBSObjectId,Status",
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> list[dict] | dict:
        """Read projects using the generated Primavera REST client wrappers."""
        try:
            client, auth_token = _resolve_rest_client(ctx, base_url=base_url, verify_ssl=verify_ssl)
            result = get_project.sync(
                client=client,
                fields=fields,
                filter_=filter_condition or None,
                order_by=order_by or None,
                **_with_auth_token(auth_token),
            )
            if result is None:
                return {"success": False, "error": "No data returned from /project endpoint."}
            return [item.to_dict() if hasattr(item, "to_dict") else item for item in result]
        except Exception as exc:
            return {"success": False, "error": f"Generated client project fetch failed: {exc}"}

    @mcp.tool()
    def rest_client_get_activities(
        ctx: Context,
        fields: str,
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> list[dict] | dict:
        """Read activities using the generated Primavera REST client wrappers."""
        try:
            client, auth_token = _resolve_rest_client(ctx, base_url=base_url, verify_ssl=verify_ssl)
            result = get_activities.sync(
                client=client,
                fields=fields,
                filter_=filter_condition or None,
                order_by=order_by or None,
                **_with_auth_token(auth_token),
            )
            if result is None:
                return {"success": False, "error": "No data returned from /activity endpoint."}
            return [item.to_dict() if hasattr(item, "to_dict") else item for item in result]
        except Exception as exc:
            return {"success": False, "error": f"Generated client activity fetch failed: {exc}"}

    @mcp.tool()
    def rest_client_get_relationships(
        ctx: Context,
        fields: str,
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> list[dict] | dict:
        return _direct_rest_get_relationships(
            ctx,
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_get_notebook_topics(
        ctx: Context,
        fields: str = "ObjectId,Name,SequenceNumber,AvailableForActivity,AvailableForProject,AvailableForWBS,AvailableForEPS",
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> list[dict] | dict:
        return _direct_rest_get_notebook_topics(
            ctx,
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_create_notebook_topics(
        ctx: Context,
        notebook_topics_json: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_notebook_topics(
            ctx,
            method="POST",
            notebook_topics_json=notebook_topics_json,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_update_notebook_topics(
        ctx: Context,
        notebook_topics_json: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_notebook_topics(
            ctx,
            method="PUT",
            notebook_topics_json=notebook_topics_json,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_delete_notebook_topic(
        ctx: Context,
        object_id: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_notebook_topics(
            ctx,
            method="DELETE",
            object_id=object_id,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_get_activity_notes(
        ctx: Context,
        fields: str,
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        """Read activity notes (notebooks assigned to activities) using direct REST."""
        try:
            resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
            params = {"Fields": fields}
            if filter_condition:
                params["Filter"] = filter_condition
            if order_by:
                params["OrderBy"] = order_by

            response = requests.get(
                f"{resolved_base_url}/activityNote",
                headers={"AuthToken": auth_token},
                cookies=cookies,
                params=params,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            return {"success": True, "activity_notes": response.json()}
        except Exception as exc:
            return {"success": False, "error": f"Activity note fetch failed: {exc}"}

    @mcp.tool()
    def rest_client_get_project_notes(
        ctx: Context,
        fields: str,
        filter_condition: str = "",
        order_by: str = "",
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        """Read project notes (notebooks assigned to projects) using direct REST."""
        try:
            resolved_base_url, auth_token, cookies = _resolve_direct_auth(ctx, base_url=base_url)
            params = {"Fields": fields}
            if filter_condition:
                params["Filter"] = filter_condition
            if order_by:
                params["OrderBy"] = order_by

            response = requests.get(
                f"{resolved_base_url}/projectNote",
                headers={"AuthToken": auth_token},
                cookies=cookies,
                params=params,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            return {"success": True, "project_notes": response.json()}
        except Exception as exc:
            return {"success": False, "error": f"Project note fetch failed: {exc}"}

    @mcp.tool()
    def rest_client_create_relationships(
        ctx: Context,
        relationships_json: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_relationships(
            ctx,
            method="POST",
            relationships_json=relationships_json,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_update_relationships(
        ctx: Context,
        relationships_json: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_relationships(
            ctx,
            method="PUT",
            relationships_json=relationships_json,
            base_url=base_url,
        )

    @mcp.tool()
    def rest_client_delete_relationship(
        ctx: Context,
        object_id: str,
        base_url: str = "",
        verify_ssl: bool = True,
    ) -> dict:
        return _direct_rest_mutate_relationships(
            ctx,
            method="DELETE",
            object_id=object_id,
            base_url=base_url,
        )