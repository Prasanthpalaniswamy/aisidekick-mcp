import os
# from urllib import response
import requests
import logging

logger = logging.getLogger(__name__)


def record_usage(
    api_key,
    tool_name
):

    product_code = (
        os.getenv(
            "PRODUCT_CODE",
            "UNKNOWN"
        )
    )

    DJANGO_API_BASE_URL = (
        os.environ.get(
            "DJANGO_API_BASE_URL"
        )
    )

    try:

        response = requests.post(

            f"{DJANGO_API_BASE_URL}/api/record-usage/",

            json={

                "tool_name":
                    tool_name,

                "product_code":
                    product_code

            },

            headers={

                "X-API-Key":
                    api_key

            },

            timeout=2

        )
        print(
            f"Usage recorded | "
            f"{response.status_code}"
        )

        if response.status_code >= 400:

            print(
                response.text
            )

    except Exception as e:

        logger.warning(
            f"Usage tracking failed: {e}"
        )