class SubscriptionError(
    Exception
):
    pass

# bEFORE PRODUCT FAMILY
# def validate_product_access(
#     user_data,
#     product_code
# ):

#     products = (

#         user_data.get(
#             "products",
#             []
#         )

#     )

#     if product_code not in products:

#         raise SubscriptionError(

#             f"{product_code} subscription required"

#         )

#     return True

# aFTER PRODUCT FAMILY
def validate_product_access(
    user_data,
    product_families
):

    product_access = user_data.get(
        "product_access",
        {}
    )

    for product_family in product_families:

        if product_family in product_access:

            return True

    raise SubscriptionError(
        "No active subscription for any supported product"
    )
# End of code