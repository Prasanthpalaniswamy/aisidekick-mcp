from mcp.server.fastmcp import FastMCP, Context

from tools.tool_registry import (
    register_tracked_tool
)

from tools.unifier.client import (
    get_projects,
    get_users,
    get_bp_records,
)

from tools.session_store import (
    UNIFIER_SESSIONS,
    get_session_key
)


def register_unifier_tools(
    mcp: FastMCP
):

    @register_tracked_tool(mcp)
    def set_unifier_credentials(
        ctx: Context,
        base_url: str,
        username: str,
        password: str,
    ):
        """
        Store Unifier session credentials.
        """

        UNIFIER_SESSIONS[
            get_session_key(ctx)
        ] = {

            "base_url": base_url,

            "username": username,

            "password": password,

            "token": None,

        }

        return {
            "success": True
        }


    @register_tracked_tool(mcp)
    def get_projects_from_unifier(
        ctx: Context,
        shell_type="Projects",
        limit=50,
        offset=0
    ):

        return get_projects(
            ctx,
            shell_type,
            limit,
            offset
        )


    @register_tracked_tool(mcp)
    def get_users_from_unifier(
        ctx: Context,
        filter_condition="",
        limit=50,
        offset=0
    ):

        return get_users(
            ctx,
            filter_condition,
            limit,
            offset
        )


    @register_tracked_tool(mcp)
    def get_bp_records_from_unifier(
        ctx: Context,
        bpname: str,
        project_number="",
    ):

        return get_bp_records(
            ctx,
            bpname,
            project_number
        )