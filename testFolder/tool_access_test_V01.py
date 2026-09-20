# tool_access_test.py

import asyncio
import json

from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

MCP_URL = "http://127.0.0.1:8002/mcp"
API_KEY = "e39f72233f9048726b34531fac80db302e707c7e1ed46f45458eb5a2d27a9650"

TEST_ARGS = {

"set_p6_credentials": {
    "username": "admin",
    "password": "admin@123",
    "base_url": "http://168.138.1.40:8206/p6ws/restapi",
    "database_name": "orclpdb.subnet10101330.vcn10101330.oraclevcn.com"
},


}
# tool_access_test.py

import asyncio
import json

from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

MCP_URL = "http://127.0.0.1:8002/mcp"
API_KEY = "e39f72233f9048726b34531fac80db302e707c7e1ed46f45458eb5a2d27a9650"

TEST_INPUTS = {


"set_p6_credentials": {
    "username": "admin",
    "password": "admin@123",
    "base_url": "http://168.138.1.40:8206/p6ws/restapi",
    "database_name": "orclpdb.subnet10101330.vcn10101330.oraclevcn.com"
},

"get_project_from_p6": {
    "project_filter": ""
},

"get_activities_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},

"get_eps_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},

"get_resources_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},

"get_resource_assignments_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},
"get_user_obs_from_p6" : {
    "fields": "ObjectId,OBSName",
    "filter_condition": "",
    "order_by": ""
}
,
"export_project_from_p6": {
    "project_object_id": 1
},

"export_projects_from_p6": {
    "project_object_ids": "1"
},

"create_eps_in_p6": {
    "eps_items_json": '[{"Id":"TEST"}]'
},

"create_resources_in_p6": {
    "resource_items_json": '[{"Id":"TEST"}]'
},
   "create_user_obs_in_p6": {
        "user_obs_items_json": "[]"
    },

"create_projects_in_p6": {
    "project_items_json": '[{}]'
},

"create_wbs_in_p6": {
    "wbs_items_json": '[{}]'
},

"create_activities_in_p6": {
    "activity_items_json":
    '[{"ProjectObjectId":1,"WBSObjectId":1}]'
},

"create_resource_assignments_in_p6": {
    "resource_assignment_items_json": '[{}]'
},

"create_resource_curves_in_p6": {
    "resource_curve_items_json": '[{}]'
},

"create_risks_in_p6": {
    "risk_items_json": '[{}]'
},

"create_activity_notes_in_p6": {
    "activity_note_items_json": '[{}]'
},

"create_activity_steps_in_p6": {
    "activity_step_items_json": '[{}]'
},

"create_calendars_in_p6": {
    "calendar_items_json": '[{}]'
},

"get_calendars_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},

"create_currencies_in_p6": {
    "currency_items_json": '[{}]'
},

"get_currencies_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},

"get_cbss_from_p6": {
    "fields": "ObjectId",
    "filter_condition": "",
    "order_by": ""
},
"export_content":{
    "content": """
[
    {
        "Project":"P6 Test",
        "Status":"Active"
    }
]
""",
    "output_file": "test_export.csv"
},

"export_content_to_pdf_tool":{
    "content": """
[
    {
        "Project":"P6 Test",
        "Status":"Active"
    }
]
""",
    "output_file": "test_export.pdf"
},


"export_content_to_docx_tool":{
    "content": """
[
    {
        "Project":"P6 Test",
        "Status":"Active"
    }
]
""",
    "output_file": "test_export.docx"
},


"convert_docx_to_pdf_tool": {

    "input_docx_file":
        "test.docx",

    "output_pdf_file":
        "test.pdf"
},

"send_email": {

    "to_emails":
        "test@example.com",

    "subject":
        "MCP Tool Test",

    "body":
        "Testing send_email tool"

},
"compress_files": {

    "input_paths":
        "test.docx,test_export.csv",

    "output_zip_file":
        "test_archive.zip"

},
"split_large_file": {

    "input_file":
        "test_export.csv"

},
    # existing entries...

    "generate_chart": {

        "content": """
[
    {
        "Month": "Jan",
        "Value": 100
    },
    {
        "Month": "Feb",
        "Value": 150
    }
]
""",

        "chart_type": "bar",

        "output_file": "test_chart.png",

        "x_field": "Month",

    },

    "generate_summary_dashboard_tool": {

        "content": """
[
    {
        "Project": "Demo",
        "Progress": 75,
        "Budget": 50000
    }
]
""",

        "output_file": "summary_dashboard.png",

    },

    "generate_table_image_tool": {

        "content": """
[
    {
        "Activity": "Design",
        "Status": "Complete"
    },
    {
        "Activity": "Build",
        "Status": "In Progress"
    }
]
""",

        "output_file": "table_output.png",

    },
}

def print_result(
tool,
status,
reason
):


    print(
        f"{status:<10} | {tool:<40} | {reason}"
    )

async def execute_tool(
    session,
    tool_name
):

    try:

        args = TEST_INPUTS.get(
            tool_name,
            {}
        )

        result = await session.call_tool(

            tool_name,

            args

        )

        if getattr(
            result,
            "isError",
            False
        ):

            error_text = str(
                result.content
            ).lower()

            if (

                "access denied" in error_text

                or

                "permission" in error_text

                or

                "not licensed" in error_text

                or

                "dashboard" in error_text

                or

                "validation error for" in error_text
                and
                "success': false" in error_text

            ):

                print_result(

                    tool_name,

                    "BLOCKED",

                    str(
                        result.content
                    )

                )

            else:

                print_result(

                    tool_name,

                    "FAILED",

                    str(
                        result.content
                    )

                )

            return


        text = ""

        if getattr(
            result,
            "structuredContent",
            None
        ):

            text = str(
                result.structuredContent
            )

        elif getattr(
            result,
            "content",
            None
        ):

            text = str(
                result.content
            )

        else:

            text = str(
                result
            )

        lower = text.lower()

        if (
            "permission" in lower
            or
            "not licensed" in lower
            or
            "access denied" in lower
        ):

            print_result(

                tool_name,

                "BLOCKED",

                text

            )

        else:

            print_result(

                tool_name,

                "PASS",

                text

            )

    except Exception as e:

        print_result(

            tool_name,

            "EXCEPTION",

            str(e)

        )
# async def execute_tool(
# session,
# tool_name
# ):


#     try:

#         args = TEST_INPUTS.get(
#             tool_name,
#             {}
#         )

#         result = await session.call_tool(

#             tool_name,

#             args

#         )

#         text = str(result)

#         lower = text.lower()

#         if "permission" in lower:

#             print_result(
#                 tool_name,
#                 "BLOCKED",
#                 text
#             )

#         elif "not licensed" in lower:

#             print_result(
#                 tool_name,
#                 "BLOCKED",
#                 text
#             )

#         elif "success" in lower:

#             print_result(
#                 tool_name,
#                 "PASS",
#                 "Executed"
#             )

#         elif "error" in lower:

#             print_result(
#                 tool_name,
#                 "FAILED",
#                 text
#             )

#         else:

#             print_result(
#                 tool_name,
#                 "UNKNOWN",
#                 text
#             )

#     except Exception as e:

#         print_result(
#             tool_name,
#             "EXCEPTION",
#             str(e)
#         )


import httpx
import traceback


async def main():

    try:

        async with streamablehttp_client(

            MCP_URL,

            headers={

                "X-API-Key": API_KEY

            }

        ) as (

            read,
            write,
            _

        ):

            async with ClientSession(
                read,
                write
            ) as session:

                await session.initialize()

                tools = await session.list_tools()

                print()
                print("=" * 90)
                print("TOOL ACCESS TEST")
                print("=" * 90)

                for tool in tools.tools:

                    await execute_tool(

                        session,
                        tool.name

                    )

    except* httpx.HTTPStatusError as eg:

        for e in eg.exceptions:

            print()
            print("=" * 90)
            print("AUTHENTICATION FAILED")
            print("=" * 90)

            code = e.response.status_code

            print(f"HTTP {code}")

            if code == 401:

                print("Invalid API Key")

            elif code == 403:

                print("API Key rejected / access denied")

            else:

                print(str(e))

    except* Exception as eg:

        print()
        print("=" * 90)
        print("CONNECTION FAILED")
        print("=" * 90)

        for e in eg.exceptions:

            print(type(e).__name__)
            print(str(e))


if __name__ == "__main__":

    asyncio.run(main())