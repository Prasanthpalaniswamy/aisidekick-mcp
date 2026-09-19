import os
from services.authentication_service import authenticate
from services.entitlement_service import validate_product_access
from contextlib import asynccontextmanager
from urllib import request

from dotenv import load_dotenv
from venv import logger
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from tools.p6_rest_client_tools import register_rest_client_tools
from tools.p6_tools import register_p6_tools
from tools.visualization_tools import register_visualization_tools
from tools.supporting_tools import register_support_tools
from tools.unifier.register import (
    register_unifier_tools
)
# from tools.supporting_tools import (
#     compress_files_to_zip,
#     convert_docx_to_pdf_content_based,
#     create_reassembly_instructions,
#     export_content_to_docx,
#     export_content_to_file,
#     export_content_to_pdf,
#     register_support_tools,
#     send_email_via_smtp,
#     split_file,
# )
# from tools.visualization_tools import (
#     generate_chart_image,
#     generate_summary_dashboard,
#     generate_table_image,
# )
# from tools.apikey_auth import validate_api_key
# from tools.apikey_auth import record_usage
from starlette.middleware.base import BaseHTTPMiddleware
from functools import wraps

from request_context import (
    current_api_key,
    current_user
)
from tools.tool_registry import (
    register_tracked_tool
)
load_dotenv()


mcp = FastMCP("AISidekick MCP", host="0.0.0.0")
# class APIKeyMiddleware(BaseHTTPMiddleware):

    # async def dispatch(
    #     self,
    #     request,
    #     call_next
    # ):

    #     api_key = request.headers.get(
    #         "X-API-Key"
    #     )
    #     try:
    #                 validate_api_key(api_key)

    #     except Exception as e:
    #         logger.warning(
    #             f"API Access Denied | Key={api_key[:8]}... | Reason={str(e)}")
    #         return JSONResponse(
    #             {
    #                         "error": str(e)
    #             },
    #                     status_code=403
    #                 )

    #     return await call_next(request)

class APIKeyMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):
        # Allow MCP authorization/discovery metadata requests
        # without API-key authentication.
        if request.url.path.startswith("/.well-known/"):
            return await call_next(request)
        api_key = request.headers.get(
            "X-API-Key"
        )
        # print("\n=== MCP REQUEST ===")
        # print("PATH:", request.url.path)
        # print("KEY:", api_key[:8] if api_key else "MISSING")
        if not api_key:

            logger.warning(
                "API Access Denied | Key=MISSING"
            )

            return JSONResponse(
                {
                    "error": "API key missing"
                },
                status_code=401
            )

        # try:

            # validate_api_key(api_key)
            # data = validate_api_key(api_key)
            # request.state.user_data = data
            # request.state.api_key = api_key

        # except Exception as e:
        try:

            user_data  = authenticate(
                api_key
            )
            PRODUCT_FAMILIES = [
                p.strip()
                for p in os.getenv(
                    "PRODUCT_FAMILIES",
                    ""
                ).split(",")
                if p.strip()
            ]

            validate_product_access(
                user_data,
                PRODUCT_FAMILIES
            )
            # PRODUCT_CODE = os.environ.get("PRODUCT_CODE")
            # validate_product_access(user_data, PRODUCT_CODE)

#             request.state.api_key = (
#                 api_key
#             )

#             request.state.user = (
            #     user_data
            # )

            request.state.api_key = api_key
            request.state.user = user_data

            current_api_key.set(
                api_key
            )

            current_user.set(
                user_data
            )
        except Exception as e:
            logger.warning(
                f"API Access Denied | Key={api_key[:8]}... | Reason={str(e)}"
            )
        

            DJANGO_API_BASE_URL = os.environ.get("DJANGO_API_BASE_URL")
            return JSONResponse(
            {
                "error": str(e),
                "portal_url":
                    f"{DJANGO_API_BASE_URL}/dashboard/",
                "support":
                    "support@aisidekick.ai"
            },
            status_code=403
        )

        return await call_next(request)

# def track_usage(tool_name):

#     def decorator(func):

#         @wraps(func)
#         def wrapper(*args, **kwargs):

#             ctx = kwargs.get("ctx")

#             api_key = getattr(
#                 ctx.request.state,
#                 "api_key",
#                 None
#             )

#             result = func(
#                 *args,
#                 **kwargs
#             )

#             if api_key:

#                 record_usage(
#                     api_key,
#                     tool_name
#                 )

#             return result

#         return wrapper
from resources.unifier.resource_registry import (
    register_unifier_resources
)
from resources.p6.resource_registry import (
    register_p6_resources
)
from prompts.unifier.prompt_registry import (
    register_unifier_prompts
)

#     return decorator
register_p6_tools(mcp)
register_p6_resources(mcp)

register_unifier_tools(mcp)
register_unifier_resources(mcp)

register_unifier_prompts(mcp)

register_support_tools(mcp)
register_visualization_tools(mcp)

print("\nREGISTERED TOOLS:\n")

try:
    import inspect

    if inspect.iscoroutinefunction(mcp.list_tools):
        print("(tool listing skipped during startup)")
    else:
        for t in mcp.list_tools():
            print(t.name)

except Exception as e:
    print(f"Unable to print tools: {e}")
# register_rest_client_tools(mcp)

# @register_tracked_tool(
#         mcp
#     )
# @mcp.tool()
# def export_content(
#     content: str,
#     output_file: str,
#     sheet_name: str = "Sheet1",
# ) -> str:
#     """Export fetched content to a .csv or .xlsx file."""
#     try:
#         return export_content_to_file(content=content, output_file=output_file, sheet_name=sheet_name)
#     except Exception as exc:
#         return f"Error exporting content: {exc}"


# @mcp.tool()
# def export_content_to_pdf_tool(
#     content: str,
#     output_file: str,
# ) -> str:
#     """Export fetched content to a .pdf file."""
#     try:
#         return export_content_to_pdf(content=content, output_file=output_file)
#     except Exception as exc:
#         return f"Error exporting content to PDF: {exc}"


# @mcp.tool()
# def export_content_to_docx_tool(
#     content: str,
#     output_file: str,
# ) -> str:
#     """Export fetched content to a .docx file."""
#     try:
#         return export_content_to_docx(content=content, output_file=output_file)
#     except Exception as exc:
#         return f"Error exporting content to DOCX: {exc}"


# @mcp.tool()
# def generate_chart(
#     content: str,
#     chart_type: str,
#     output_file: str,
#     x_field: str,
#     y_field: str = "",
#     title: str = "Chart",
#     group_by: str = "",
# ) -> str:
#     """Generate a chart image (.png) from fetched JSON content."""
#     try:
#         return generate_chart_image(
#             content=content,
#             chart_type=chart_type,
#             output_file=output_file,
#             x_field=x_field,
#             y_field=y_field,
#             title=title,
#             group_by=group_by,
#         )
#     except Exception as exc:
#         return f"Error generating chart: {exc}"


# @mcp.tool()
# def generate_summary_dashboard_tool(
#     content: str,
#     output_file: str,
#     title: str = "Summary Dashboard",
#     metric_fields: str = "",
#     category_field: str = "",
#     top_n: int = 10,
# ) -> str:
#     """Generate a summary dashboard PNG from fetched JSON content."""
#     try:
#         return generate_summary_dashboard(
#             content=content,
#             output_file=output_file,
#             title=title,
#             metric_fields=metric_fields,
#             category_field=category_field,
#             top_n=top_n,
#         )
#     except Exception as exc:
#         return f"Error generating summary dashboard: {exc}"


# @mcp.tool()
# def generate_table_image_tool(
#     content: str,
#     output_file: str,
#     title: str = "Data Table",
#     columns: str = "",
#     max_rows: int = 20,
# ) -> str:
#     """Generate a table image PNG from fetched JSON content."""
#     try:
#         return generate_table_image(
#             content=content,
#             output_file=output_file,
#             title=title,
#             columns=columns,
#             max_rows=max_rows,
#         )
#     except Exception as exc:
#         return f"Error generating table image: {exc}"


# @mcp.tool()
# def convert_docx_to_pdf_tool(
#     input_docx_file: str,
#     output_pdf_file: str,
# ) -> str:
#     """Convert a DOCX file into a simple content-based PDF."""
#     try:
#         return convert_docx_to_pdf_content_based(
#             input_docx_file=input_docx_file,
#             output_pdf_file=output_pdf_file,
#         )
#     except Exception as exc:
#         return f"Error converting DOCX to PDF: {exc}"


# @mcp.tool()
# def send_email(
#     to_emails: str,
#     subject: str,
#     body: str,
#     attachment_paths: str = "",
# ) -> str:
#     """Send a plain-text email with optional attachments using configured SMTP settings."""
#     try:
#         attachments = [path.strip() for path in attachment_paths.split(",") if path.strip()]
#         return send_email_via_smtp(
#             smtp_host="smtp.gmail.com",
#             smtp_port=587,
#             username="productivepmo@gmail.com",
#             password="jkxz gvwr ijcu jdhc",
#             sender_email="productivepmo@gmail.com",
#             to_emails=to_emails,
#             subject=subject,
#             body=body,
#             attachment_paths=attachments,
#             use_starttls=True,
#         )
#     except Exception as exc:
#         return f"Error sending email: {exc}"


# @mcp.tool()
# def compress_files(
#     input_paths: str,
#     output_zip_file: str,
# ) -> str:
#     """Compress one or more files into a ZIP archive."""
#     try:
#         files = [path.strip() for path in input_paths.split(",") if path.strip()]
#         return compress_files_to_zip(files, output_zip_file)
#     except Exception as exc:
#         return f"Error compressing files: {exc}"


# @mcp.tool()
# def split_large_file(
#     input_file: str,
#     output_dir: str = "",
#     part_size_mb: int = 10,
# ) -> dict:
#     """Split a large file into smaller parts for transfer."""
#     try:
#         result = split_file(input_file=input_file, output_dir=output_dir, part_size_mb=part_size_mb)
#         result["reassembly_instructions"] = create_reassembly_instructions(
#             original_file_name=os.path.basename(input_file),
#             part_files=result["parts"],
#         )
#         return result
#     except Exception as exc:
#         return {"error": str(exc)}


async def healthcheck(request):
    return JSONResponse(
        {
            "status": "ok",
            "message": "AISidekick MCP is running",
            "mcp_endpoint": "/mcp",
        }
    )


mcp_app = mcp.streamable_http_app()


@asynccontextmanager
async def lifespan(app):
    async with mcp.session_manager.run():
        yield


app = Starlette(
    routes=[
        Route("/health", healthcheck),
        Mount("/", app=mcp_app),
    ],
    lifespan=lifespan,
)
app.add_middleware(
    APIKeyMiddleware
)

if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "http").lower()
    print(f"Starting AISidekick MCP with transport: {transport}")

    if transport in ["http", "https"]:
        import uvicorn

        port = int(os.environ.get("PORT", 8002))

        uvicorn.run(
            "server:app",
            host="0.0.0.0",
            port=port,
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
    else:
        mcp.run()