from typing import Optional, Dict, Any, List

from mcp.server.fastmcp import FastMCP, Context
from tools.tool_registry import register_tracked_tool

from tools.unifier.client import (
    get_projects,
    get_data_elements,
    get_data_definitions,
    get_users,
    get_bp_records,
    create_data_elements,
)

from tools.session_store import (
    UNIFIER_SESSIONS,
    get_session_key
)

from tools.unifier.client import (
    validate_base_url,
    validate_username,
    validate_password
)
import logging
from typing import Literal, Optional

logger = logging.getLogger(__name__)
DfType = Literal["Basic", "Cost Codes", "Data Picker"]

def safe_register(tool_name, register_fn):

    try:
        register_fn()

        logger.info(
            f"✓ Registered tool: {tool_name}"
        )

    except Exception as e:

        logger.exception(
            f"✗ Failed registering tool {tool_name}: {e}"
        )

def register_unifier_tools(
    mcp: FastMCP
):

    #
    # SESSION
    #

    @register_tracked_tool(mcp)
    def set_unifier_credentials(
        ctx: Context,
        base_url: str,
        username: str,
        password: str
    ):
        """
        Configure and store Oracle Primavera Unifier credentials for the current session.

        Use this tool before calling any Unifier data retrieval or creation tools.

        Parameters:
        - base_url: Unifier REST base URL ending with /ws/rest/service/v1
        - username: Integration username (typically starts with $$)
        - password: Integration user password

        Returns:
        - success: true if credentials were validated and stored
        """

        UNIFIER_SESSIONS[
            get_session_key(ctx)
        ] = {

            "base_url":
                validate_base_url(base_url),

            "username":
                validate_username(username),

            "password":
                validate_password(password),

            "token":
                None
        }

        return {
            "success": True
        }


    @register_tracked_tool(mcp)
    def get_unifier_credentials_status(
        ctx: Context
    ):
        """
    Check whether Unifier credentials are configured for the current session.

    Returns:
    - configured: true if credentials are already stored
        """

        return {

            "configured":

            get_session_key(ctx)
            in
            UNIFIER_SESSIONS
        }


    @register_tracked_tool(mcp)
    def clear_unifier_session(
        ctx: Context
    ):
        """
    Clear stored Unifier credentials and authentication token for the current session.

    Use this when switching environments or users.

    Returns:
    - success: true if session data was cleared
        """

        UNIFIER_SESSIONS.pop(
            get_session_key(ctx),
            None
        )

        return {
            "success": True
        }

    #
    # READ
    #

    # @register_tracked_tool(mcp)
    # def get_projects_tool_in_unifier(
    #     ctx: Context,
    #     shell_type: str = "Projects",
    #     limit: Optional[int] = None,
    #     offset: int = 0
    # ):
    #     return get_projects(
    #         ctx,
    #         shell_type,
    #         limit,
    #         offset
    #     )

    def register_get_projects():

        @register_tracked_tool(mcp)
        def get_projects_tool_in_unifier(
            ctx: Context,
            shell_type: str = "Projects",
            limit: int | None = None,
            offset: int = 0
        ):
            """
    Retrieve project shells from Oracle Primavera Unifier.

    Parameters:
    - shell_type: Shell category to retrieve (default: Projects)
    - limit: Maximum number of records
    - offset: Starting position for pagination

    Returns:
    - Project shell data from Unifier
    - Pagination information when applicable
            """
            
            return get_projects(
                ctx,
                shell_type,
                limit,
                offset
            )


    safe_register(
        "get_projects_tool_in_unifier",
        register_get_projects
    )



    @register_tracked_tool(mcp)
    def get_data_elements_tool_in_unifier(
        ctx: Context,
        filter_options: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: int = 0
    ):
        """
    Retrieve Data Elements configured in Oracle Primavera Unifier.

    Parameters:
    - filter_options:
        data_element
        data_definition
        form_label
        description
        tooltip

    - limit: Maximum records
    - offset: Pagination offset

    Returns:
    - Matching data element definitions
        """
        return get_data_elements(
            ctx,
            filter_options,
            limit,
            offset
        )
    from typing import Literal
  


    @register_tracked_tool(mcp)
    def get_data_definitions_tool_in_unifier(
        ctx: Context,
        df_type: Optional[DfType] = None,
        filter_options: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: int = 0
    ):
        """
    Retrieve Data Definitions from Oracle Primavera Unifier.

    Parameters:
    - df_type:
        Basic
        Cost Codes
        Data Picker

    - filter_options:
        name
        data_source

    - limit: Maximum records
    - offset: Pagination offset

    Returns:
    - Matching data definitions
        """
        return get_data_definitions(
            ctx,
            df_type,
            filter_options,
            limit,
            offset
        )


    # @register_tracked_tool(mcp)
    # def get_users_tool_in_unifier(
    #     ctx: Context,
    #     filter_condition: Optional[dict] = None,
    #     limit: Optional[int] = None,
    #     offset: int = 0
    # ):
    #     return get_users(
    #         ctx,
    #         filter_condition,
    #         limit,
    #         offset
    #     )

    def register_get_users():

        @register_tracked_tool(mcp)
        def get_users_tool_in_unifier(
            ctx: Context,
            filter_condition: str | None = None,
            limit: int | None = None,
            offset: int = 0
        ):
            """
                Retrieve users from Oracle Primavera Unifier.

                Parameters:
                - filter_condition:
                    Unifier user filtering expression

                - limit: Maximum records
                - offset: Pagination offset

                Returns:
                - User information matching filter criteria
            """
            return get_users(
                ctx,
                filter_condition,
                limit,
                offset
            )


    safe_register(
        "get_users_tool_in_unifier",
        register_get_users
    )

    @register_tracked_tool(mcp)
    def get_bp_records_tool_in_unifier(
        ctx: Context,
        bpname: str,
        project_number: Optional[str] = None,
        options: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: int = 0
    ):
        """
    Retrieve Business Process (BP) records from Oracle Primavera Unifier.

    Parameters:
    - bpname: Business Process name
    - project_number: Project identifier (optional)
    - options: Additional Unifier query options
    - limit: Maximum records
    - offset: Pagination offset

    Returns:
    - BP records at Company or Project level
        """
        return get_bp_records(
            ctx,
            bpname,
            project_number,
            options,
            limit,
            offset
        )


    #
    # CREATE
    #



    # @register_tracked_tool(mcp)
    # def create_data_elements_tool_in_unifier(
    #     ctx: Context,
    #     elements_list: List[Dict[str, Any]]
    # ):
    #     """
    # Create custom Data Elements in Oracle Primavera Unifier.

    # Parameters:
    # - elements_list:
    #     List of data element definitions.

    # Example:
    # [
    #     {
    #         "data_element": "DE_TEST",
    #         "form_label": "Test Field"
    #     }
    # ]

    # Returns:
    # - Unifier creation response
    #     """
    #     return create_data_elements(
    #         ctx,
    #         elements_list
    #     )



    @register_tracked_tool(mcp)
    def create_data_elements_tool_in_unifier(
        ctx: Context,
        elements_list: List[Dict[str, Any]]
    ):
        """
        Create custom Data Elements in Oracle Primavera Unifier.

        Mandatory fields:
        - data_element
        - data_definition
        - form_label

        Conditional fields:
        - Image Picker → height
        - SYS Rich Text → height
        - textarea → no_of_lines
        - Decimal Amount → decimal_format
        - SYS Numeric Query Based → hide_currency_symbol

        Example:

        [
            {
                "data_element":"sampleDE",
                "data_definition":"Decimal Amount",
                "form_label":"Sample Decimal Element",
                "description":"Test DE",
                "decimal_format":"5"
            }
        ]

        Returns:
        - Created elements
        - Partial success messages
        - Validation details
        """

        return create_data_elements(
            ctx,
            elements_list
        )