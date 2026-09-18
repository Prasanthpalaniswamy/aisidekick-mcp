from mcp.server.fastmcp import FastMCP


def register_unifier_prompts(
    mcp: FastMCP
):

    @mcp.prompt()
    def create_data_elements_prompt():

        return """
Create Oracle Primavera Unifier Data Elements.

Rules:
- data_element required
- data_definition required
- form_label required

Conditional:
- Decimal Amount → decimal_format
- Image Picker → height

Return valid JSON only.
"""