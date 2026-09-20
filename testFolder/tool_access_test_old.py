# tool_access_test.py

import asyncio
import json

from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

MCP_URL = "http://127.0.0.1:8002/mcp"
API_KEY = "40061799f3a69152343af4aa47c1c11089a91946d19be5e475ce883aec28fc42"



TEST_ARGS = {

    # -------------------
    # SESSION
    # -------------------

    "set_p6_credentials": {
        "username": "admin",
        "password": "admin@123",
        "base_url": "http://168.138.1.40:8206/p6ws/restapi",
        "database_name": "orclpdb.subnet10101330.vcn10101330.oraclevcn.com"
    },

    "get_p6_credentials_status": {},

    "clear_p6_session": {},

    # -------------------
    # READ
    # -------------------

    "get_project_from_p6": {
        "project_filter": ""
    },

    "get_activities_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_eps_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_resources_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_resource_assignments_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_user_obs_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_calendars_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_currencies_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    "get_cbss_from_p6": {
        "fields": "ObjectId",
        "filter_condition": "",
        "order_by": "",
    },

    # -------------------
    # EXPORT
    # -------------------

    "export_project_from_p6": {
        "project_object_id": 1
    },

    "export_projects_from_p6": {
        "project_object_ids": "1"
    },

    # -------------------
    # CREATE
    # -------------------

    "create_eps_in_p6": {
        "eps_items_json": "[]"
    },

    "create_resources_in_p6": {
        "resource_items_json": "[]"
    },

    "create_user_obs_in_p6": {
        "user_obs_items_json": "[]"
    },

    "create_projects_in_p6": {
        "project_items_json": "[]"
    },

    "create_wbs_in_p6": {
        "wbs_items_json": "[]"
    },

    "create_activities_in_p6": {
        "activity_items_json": "[]"
    },

    "create_resource_assignments_in_p6": {
        "resource_assignment_items_json": "[]"
    },

    "create_resource_curves_in_p6": {
        "resource_curve_items_json": "[]"
    },

    "create_risks_in_p6": {
        "risk_items_json": "[]"
    },

    "create_activity_notes_in_p6": {
        "activity_note_items_json": "[]"
    },

    "create_activity_steps_in_p6": {
        "activity_step_items_json": "[]"
    },

    "create_calendars_in_p6": {
        "calendar_items_json": "[]"
    },

    "create_currencies_in_p6": {
        "currency_items_json": "[]"
    },

}


async def run():

async with stdio_client(...) as (read_stream, write_stream):
    async with ClientSession(
        read_stream,
        write_stream,
    ):

        tools = await session.list_tools()

        print("\nTOOL ACCESS TEST\n")

        for tool in tools.tools:

            args = TEST_ARGS.get(
                tool.name,
                {}
            )

            try:

                result = await session.call_tool(
                    tool.name,
                    args
                )

                txt = str(result)

                if "Access denied" in txt:

                    print(
                        f"ACCESS BLOCKED | {tool.name}"
                    )

                elif "validation error" in txt.lower():

                    print(
                        f"BAD TEST DATA | {tool.name}"
                    )

                else:

                    print(
                        f"PASS | {tool.name}"
                    )

            except Exception as e:

                print(
                    f"ERROR | {tool.name} | {e}"
                )


asyncio.run(run())