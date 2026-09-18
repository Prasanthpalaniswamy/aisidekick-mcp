import threading
import requests
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def _send_usage(
    api_key,
    tool_name,
    product_code
):

    try:

        django_url = os.getenv(
            "DJANGO_API_BASE_URL"
        )
        # print(f"Usage tracking | "
        #     f"Recording usage for tool: {tool_name} | "
        #     f"Product code: {product_code} | "
        #     f"URL: {django_url}/api/record-usage/"
        # )

        response =requests.post(

            f"{django_url}/api/record-usage/",

            headers={
                "X-API-Key":
                    api_key, 
                "Content-Type":
                    "application/json"
            },

            json={

                "product_code":
                    product_code,

                "tool_name":
                    tool_name

            },

            timeout=5

        )
        # print(
        #             "USAGE RESPONSE:",
        #             response.status_code,
        #             response.text
        # )
    except Exception as e:

        print(
            f"Usage tracking failed: {e}"
        )


def track_usage(
    api_key,
    tool_name,
    product_code
):

    thread = threading.Thread(

        target=_send_usage,

        kwargs={

            "api_key":
                api_key,

            "tool_name":
                tool_name,

            "product_code":
                product_code

        },

        daemon=True

    )

    thread.start()