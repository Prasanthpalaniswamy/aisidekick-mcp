from datetime import datetime
# from django.utils.dateparse import parse_datetime


TOOL_ACCESS = {

    # -------------------------
    # SESSION / SETUP
    # -------------------------

    "set_p6_credentials": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_p6_credentials_status": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "clear_p6_session": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    # -------------------------
    # READ TOOLS
    # -------------------------

    "get_project_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_activities_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_eps_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_resources_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_resource_assignments_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_user_obs_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_calendars_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_currencies_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "get_cbss_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    # -------------------------
    # EXPORT
    # -------------------------

    "export_project_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    "export_projects_from_p6": {
        "products": ["P6"],
        "capability": "VIEWER",
    },

    # -------------------------
    # CREATE / EXECUTE
    # -------------------------

    "create_eps_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_resources_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_user_obs_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_projects_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_wbs_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_activities_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_resource_assignments_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_resource_curves_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_risks_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_activity_notes_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_activity_steps_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_calendars_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

    "create_currencies_in_p6": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },
    
     "export_content": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

     "split_large_file": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "compress_files": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "send_email": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "convert_docx_to_pdf_tool": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "export_content_to_docx_tool": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "export_content_to_pdf_tool": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "generate_chart": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "generate_table_image_tool": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

 "generate_summary_dashboard_tool": {
        "products": ["P6"],
        "capability": "OPERATOR",
    },

# -------------------------
# UNIFIER - SESSION
# -------------------------

"set_unifier_credentials": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"get_unifier_credentials_status": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"clear_unifier_session": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

# -------------------------
# UNIFIER - READ
# -------------------------

"get_projects_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"get_data_elements_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"get_data_definitions_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"get_users_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

"get_bp_records_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "VIEWER",
},

# -------------------------
# UNIFIER - CREATE
# -------------------------

"create_data_elements_tool_in_unifier": {
    "products": ["UNIFIER"],
    "capability": "OPERATOR",
},

}
LEVELS = {

    "VIEWER": 1,

    "OPERATOR": 2,

    "PROFESSIONAL": 3,

    "ENTERPRISE": 4
}

# def can_execute(
#     product_access,
#     tool_name
# ):

#     tool = (
#         TOOL_ACCESS.get(
#             tool_name
#         )
#     )

#     if not tool:

#         return (
#             False,
#             "Tool not registered"
#         )

#     products = (
#         tool["products"]
#     )

#     required = (
#         tool["capability"]
#     )
#     for product in products:
#         subscription = (
#             product_access.get(
#                 product
#             )
#         )

#         if not subscription:

#             return (
#                 False,
#                 f"{product} subscription required"
#             )

#         expiry = (
#             subscription.get(
#                 "expires_at"
#             )
#         )

#         if expiry:

#             expires_at = (

#                 datetime
#                 .fromisoformat(
#                     expiry
#                 )

#             )

#             if expires_at < datetime.now(
#                 expires_at.tzinfo
#             ):

#                 return (

#                     False,

#                     f"{product} subscription expired"

#                 )

#         actual = (

#             subscription[
#                 "capability"
#             ]

#         )

#     allowed = (

#         LEVELS[
#             actual
#         ]

#         >=

#         LEVELS[
#             required
#         ]

#     )

#     if not allowed:

#         return (

#             False,

#             f"{required} access required"

#         )

#     return (
#         True,
#         None
#     )

from datetime import datetime


def can_execute(
    product_access,
    tool_name
):

    tool = TOOL_ACCESS.get(tool_name)

    if not tool:
        return (
            False,
            "Tool not registered"
        )

    products = tool.get(
        "products",
        []
    )

    required = tool["capability"]

    for product in products:

        subscription = product_access.get(
            product
        )

        if not subscription:
            continue

        expiry = subscription.get(
            "expires_at"
        )

        if expiry:

            expires_at = datetime.fromisoformat(
                expiry
            )

            if expires_at < datetime.now(
                expires_at.tzinfo
            ):
                continue

        actual = subscription.get(
            "capability"
        )

        if not actual:
            continue

        if LEVELS[actual] >= LEVELS[required]:

            return (
                True,
                None
            )

    if len(products) == 1:

        product = products[0]

        return (
            False,
            f"{product} subscription required"
        )

    return (
        False,
        "Required product access not available"
    )

def get_tool_product(
    tool_name
):

    tool = TOOL_ACCESS.get(
        tool_name
    )

    if not tool:

        return None

    products = tool.get(
        "products",
        []
    )

    if not products:

        return None

    return products[0]


# end of code