from mcp.server.fastmcp import FastMCP


def register_p6_resources(
    mcp: FastMCP
):

    @mcp.resource(
        "p6://projects"
    )
    def p6_projects_resource():

        """
        Reference guide for P6 Project listing.
        """

        return """
Oracle Primavera P6 Project Listing

Purpose:
Retrieve projects from P6.

Typical hierarchy:

EPS
 └── Project
      └── WBS
           └── Activity

Common fields:

projectId
projectCode
projectName
status
plannedStartDate
plannedFinishDate
epsId

Usage:

1. Authenticate using set_p6_credentials
2. Call get_project_from_p6
3. Filter by EPS if needed

Example output:

[
 {
   "projectId":123,
   "projectCode":"PRJ001",
   "projectName":"Airport Expansion"
 }
]
"""