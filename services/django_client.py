import os
import requests
from dotenv import load_dotenv
load_dotenv()


DJANGO_API_BASE_URL = os.getenv(
    "DJANGO_API_BASE_URL"
)


# def validate_key(api_key):
#     print("\n=== VALIDATE API KEY START ===")

#     print("URL:", f"{DJANGO_API_BASE_URL}/api/validate-key/")
#     print("KEY:", api_key[:8])

#     response = requests.get(

#         f"{DJANGO_API_BASE_URL}/api/validate-key/",

#         headers={
#             "X-API-Key": api_key
#         },

#         timeout=10
#     )

#     response.raise_for_status()

#     return response.json()

def validate_key(api_key):

    # print("\n=== VALIDATE API KEY START ===")

    # print("URL:", f"{DJANGO_API_BASE_URL}/api/validate-key/")
    # print("KEY:", api_key[:8])

    response = requests.get(
        f"{DJANGO_API_BASE_URL}/api/validate-key/",
        headers={
            "X-API-Key": api_key
        },
        timeout=10
    )

    # print("STATUS:", response.status_code)
    # print("BODY:", response.text)

    if response.status_code != 200:
        raise Exception(
            f"Authentication failed | "
            f"HTTP={response.status_code} | "
            f"{response.text}"
        )

    data = response.json()

    # print("DATA:", data)

    product_access = data.get(
        "product_access",
        {}
    )

    # print("PRODUCT_ACCESS:", product_access)

    # if "P6" not in product_access:

    #     raise Exception(
    #         f"P6 missing. Available={list(product_access.keys())}"
    #     )

    # # print("=== VALIDATE SUCCESS ===\n")

    return data




def record_usage(
    api_key,
    tool_name,
    product_code
):

    requests.post(

        f"{DJANGO_API_BASE_URL}/api/record-usage/",

        headers={
            "X-API-Key": api_key
        },

        data={

            "product_code":
                product_code,

            "tool_name":
                tool_name

        },

        timeout=5
    )