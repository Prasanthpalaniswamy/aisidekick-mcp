from mcp.server.fastmcp import FastMCP


def register_p6_prompts(
    mcp: FastMCP
):

    @mcp.prompt()
    def list_p6_projects():

        return """
Goal:
Retrieve projects from Primavera P6.

Process:

1. Verify credentials exist:
   get_p6_credentials_status

2. If missing:
   request set_p6_credentials

3. Execute:
   get_project_from_p6

4. Present:

- Project Code
- Project Name
- Status
- Dates

Do not return raw API output unless requested.
Prefer concise summaries.
"""