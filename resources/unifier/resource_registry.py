from mcp.server.fastmcp import FastMCP


def register_unifier_resources(
    mcp: FastMCP
):

    @mcp.resource(
        "unifier://bp-guide"
    )
    def bp_guide():

        return """
Supported Business Processes:

- Change Order
- RFI
- Issue
- Contract
"""



    @mcp.resource(
        "unifier://data-elements-guide"
    )
    def data_elements():

        return """
Required:
data_element
data_definition
form_label

Conditional:
Image Picker → height
Decimal Amount → decimal_format
"""