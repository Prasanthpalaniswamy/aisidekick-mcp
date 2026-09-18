import os

from dotenv import load_dotenv
import requests

import os
import requests

load_dotenv()
DJANGO_API_BASE_URL = os.getenv(
    "DJANGO_API_BASE_URL"
)

PRODUCT_CODE = os.getenv(
    "PRODUCT_CODE"
)
def record_usage(
    api_key,
    tool_name
):

    try:

        requests.post(
            f"{DJANGO_API_BASE_URL}/api/record-usage/",
            headers={
                "X-API-Key": api_key
            },
            data={
                "product_code": PRODUCT_CODE,
                "tool_name": tool_name
            },
            timeout=5
        )

    except Exception:

        pass


def validate_api_key(api_key):
    load_dotenv()

    DJANGO_API_BASE_URL = os.environ.get("DJANGO_API_BASE_URL")
    response = requests.get(
        # "https://aisidekick.onrender.com/api/validate-key/",
        f"{DJANGO_API_BASE_URL}/api/validate-key/",
        headers={
            "X-API-Key": api_key
        },
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(
            "Authentication failed"
        )
        # return False

    data = response.json()
    if not data.get("valid"):
        raise Exception(
            data.get("message",
            "Invalid API Key"
        ))
    
    # if "P6" not in data["products"]:
    #     raise Exception(
    #         "P6 subscription required"
    #     )

    
    
    product_access = data.get(
    "product_access",
    {}
)

    if "P6" not in product_access:

        raise Exception(
            "P6 subscription required"
        )
    


    return data