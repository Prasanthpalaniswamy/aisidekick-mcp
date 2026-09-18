from services.django_client import validate_key
from venv import logger

class AuthenticationError(
    Exception
):
    pass


def authenticate(
    api_key
):

    try:

        data = validate_key(
            api_key
        )


    except Exception as e:
        logger.exception(
                    "validate_key() failed: %s",
                    str(e)
                )

        raise AuthenticationError(
                    f"Authentication failed: {str(e)}"
                )

        # raise AuthenticationError(
        #     "Authentication failed"
        # )

    if not data.get(
        "valid"
    ):

        raise AuthenticationError(

            data.get(
                "message",
                "Invalid API Key"
            )

        )

    return data