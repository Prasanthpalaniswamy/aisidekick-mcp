import os
import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv(
    "DJANGO_API_BASE_URL"
)

API_KEY = os.getenv(
    "DJANGO_API_KEY"
)


def validate():

    response = requests.get(

        f"{BASE_URL}/api/validate-key/",

        headers={
            "X-API-Key": API_KEY
        },

        timeout=10
    )

    print("\n===== VALIDATE =====")

    print(
        "Status:",
        response.status_code
    )

    print(
        response.json()
    )


def record_usage():

    response = requests.post(

        f"{BASE_URL}/api/record-usage/",

        headers={
            "X-API-Key": API_KEY
        },

        json={

            "tool_name":
                "get_project_from_p6",

            "product_code":
                "P6"
        },

        timeout=10
    )

    print("\n===== RECORD USAGE =====")

    print(
        "Status:",
        response.status_code
    )

    print(
        response.json()
    )


if __name__ == "__main__":

    validate()

    record_usage()