from functools import wraps
import os
from dotenv import load_dotenv
load_dotenv()
from request_context import (
    current_api_key,
    current_user
)

from services.usage_service import (
    track_usage
)

from tools.permissions import (
    can_execute,
    get_tool_product
)


def register_tracked_tool(
    mcp
):

    def decorator(
        func
    ):

        @wraps(func)

        def wrapper(
            *args,
            **kwargs
        ):

            user = (
                current_user.get()
            )

            api_key = (
                current_api_key.get()
            )

            #
            # AUTHORIZATION
            #

            if user:

                allowed, message = (

                    can_execute(

                        user.get(
                            "product_access",
                            {}
                        ),

                        func.__name__

                    )

                )

                if not allowed:

                    return {

                        "success": False,

                        "error": message,

                        "portal_url":

                            f"{os.getenv('DJANGO_API_BASE_URL')}/dashboard/"

                    }

            #
            # EXECUTION
            #

            try:

                result = func(
                    *args,
                    **kwargs
                )

            except Exception as e:

                return {

                    "success": False,

                    "error": str(e)

                }

            #
            # USAGE TRACKING
            #

            try:

                if api_key:

                    track_usage(

                        api_key=
                            api_key,

                        tool_name=
                            func.__name__,

                         product_code=
                get_tool_product(
                    func.__name__
                )


                    )

            except Exception as e:

                print(

                    f"Usage tracking failed: {e}"

                )

            return result

        return (

            mcp.tool()(

                wrapper

            )

        )

    return decorator


# end of code