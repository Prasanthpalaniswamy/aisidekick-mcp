import base64
import logging
import os
from datetime import datetime, timezone
from typing import Any

import requests
from mcp.server.fastmcp import Context

from request_context import current_api_key
from tools.session_store import (
    get_p6_session,
    set_p6_session,
)

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT_SECONDS = 30


def _generate_auth_token(
    username: str,
    password: str,
) -> str:
    credentials = f"{username}:{password}"

    return base64.b64encode(
        credentials.encode("utf-8")
    ).decode("utf-8")

def _login_auth(
    auth_token: str,
    base_url: str,
    database_name: str,
) -> requests.cookies.RequestsCookieJar | None:

    url = f"{base_url.rstrip('/')}/login"

    try:
        response = requests.post(
            url,
            headers={
                "AuthToken": auth_token,
            },
            params={
                "DatabaseName": database_name,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        response.raise_for_status()

        return response.cookies

    except requests.RequestException as exc:
        logger.error(
            "P6 login failed: %s",
            exc,
        )

        return None

def _get_connection_from_django(
    connection_id: int,
) -> dict[str, Any]:

    api_key = current_api_key.get()

    if not api_key:
        return {
            "success": False,
            "error": "Authenticated API key is not available.",
        }

    django_base_url = os.environ.get(
        "DJANGO_API_BASE_URL"
    )

    if not django_base_url:
        return {
            "success": False,
            "error": "DJANGO_API_BASE_URL is not configured.",
        }

    url = (
        f"{django_base_url.rstrip('/')}"
        f"/api/mcp/p6-connection/"
    )

    try:
        response = requests.get(
            url,
            headers={
                "X-API-Key": api_key,
            },
            params={
                "connection_id": connection_id,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("valid"):
            return {
                "success": False,
                "error": data.get(
                    "message",
                    "P6 connection could not be retrieved.",
                ),
            }

        connection = data.get("connection")

        if not connection:
            return {
                "success": False,
                "error": "Django returned no P6 connection details.",
            }

        return {
            "success": True,
            "connection": connection,
        }

    except requests.HTTPError as exc:

        status_code = (
            exc.response.status_code
            if exc.response is not None
            else None
        )

        logger.warning(
            "Django P6 connection lookup failed | "
            "connection_id=%s | status=%s",
            connection_id,
            status_code,
        )

        try:
            error_data = exc.response.json()
            message = error_data.get(
                "message",
                "Unable to retrieve P6 connection.",
            )
        except Exception:
            message = (
                "Unable to retrieve the requested P6 connection."
            )

        return {
            "success": False,
            "error": message,
        }

    except requests.RequestException as exc:

        logger.error(
            "Django P6 connection request failed: %s",
            exc,
        )

        return {
            "success": False,
            "error": (
                "Unable to contact the AI Sidekick "
                "connection service."
            ),
        }

    except ValueError:

        return {
            "success": False,
            "error": (
                "AI Sidekick returned an invalid response "
                "while retrieving the P6 connection."
            ),
        }

def get_p6_connection_session(
    ctx: Context,
    connection_id: int,
) -> dict[str, Any]:

    # ---------------------------------------------------------
    # 1. Check session cache
    # ---------------------------------------------------------

    existing_session = get_p6_session(
        ctx,
        connection_id,
    )

    if existing_session:
        return {
            "success": True,
            "session": existing_session,
            "source": "session_cache",
        }

    # ---------------------------------------------------------
    # 2. Retrieve selected connection from Django
    # ---------------------------------------------------------

    result = _get_connection_from_django(
        connection_id,
    )

    if not result["success"]:
        return result

    connection = result["connection"]

    # ---------------------------------------------------------
    # 3. Generate P6 authentication token
    # ---------------------------------------------------------

    auth_token = _generate_auth_token(
        connection["username"],
        connection["password"],
    )

    # ---------------------------------------------------------
    # 4. Login to selected P6 environment
    # ---------------------------------------------------------

    cookies = _login_auth(
        auth_token,
        connection["base_url"],
        connection["database_name"],
    )

    if not cookies:
        return {
            "success": False,
            "error": (
                f"Unable to login to P6 connection "
                f"'{connection.get('name', connection_id)}'."
            ),
        }

    # ---------------------------------------------------------
    # 5. Build session
    # ---------------------------------------------------------

    session = {
        "connection_id": connection_id,
        "name": connection["name"],
        "base_url": connection["base_url"],
        "database_name": connection["database_name"],
        "username": connection["username"],
        "auth_token": auth_token,
        "cookies": cookies,
        # "authenticated_at": datetime.utcnow().isoformat(),
        "authenticated_at": datetime.now(timezone.utc).isoformat(),
    }

    # ---------------------------------------------------------
    # 6. Cache session
    # ---------------------------------------------------------

    set_p6_session(
        ctx,
        connection_id,
        session,
    )

    return {
        "success": True,
        "session": session,
        "source": "new_login",
    }

# import os
# import logging
# from typing import Any
# from datetime import datetime
# import requests
# from mcp.server.fastmcp import Context

# from tools.session_store import (
#     get_p6_session,
# )
# from request_context import current_api_key

# import logging
# from typing import Any

# import requests
# from mcp.server.fastmcp import Context

# from tools.session_store import (
#     get_p6_session,
#     set_p6_session,
# )

# logger = logging.getLogger(__name__)

# REQUEST_TIMEOUT_SECONDS = 30


# def _generate_auth_token(
#     username: str,
#     password: str,
# ) -> str:
#     import base64

#     credentials = f"{username}:{password}"

#     return base64.b64encode(
#         credentials.encode("utf-8")
#     ).decode("utf-8")


# def _login_auth(
#     auth_token: str,
#     base_url: str,
#     database_name: str,
# ) -> requests.cookies.RequestsCookieJar | None:

#     url = f"{base_url.rstrip('/')}/login"

#     try:
#         response = requests.post(
#             url,
#             headers={
#                 "AuthToken": auth_token,
#             },
#             params={
#                 "DatabaseName": database_name,
#             },
#             timeout=REQUEST_TIMEOUT_SECONDS,
#         )

#         response.raise_for_status()

#         return response.cookies

#     except requests.RequestException as exc:
#         logger.error(
#             "P6 login failed: %s",
#             exc,
#         )

#         return None


# def _get_connection_from_django(
#     connection_id: int,
# ) -> dict[str, Any]:

#     api_key = current_api_key.get()

#     if not api_key:
#         return {
#             "success": False,
#             "error": "Authenticated API key is not available.",
#         }

#     django_base_url = os.environ.get(
#         "DJANGO_API_BASE_URL"
#     )

#     if not django_base_url:
#         return {
#             "success": False,
#             "error": "DJANGO_API_BASE_URL is not configured.",
#         }

#     url = (
#         f"{django_base_url.rstrip('/')}"
#         f"/api/mcp/p6-connection/"
#     )

#     try:

#         response = requests.get(
#             url,
#             headers={
#                 "X-API-Key": api_key,
#             },
#             params={
#                 "connection_id": connection_id,
#             },
#             timeout=REQUEST_TIMEOUT_SECONDS,
#         )

#         response.raise_for_status()

#         data = response.json()

#         if not data.get("valid"):
#             return {
#                 "success": False,
#                 "error": data.get(
#                     "message",
#                     "P6 connection could not be retrieved.",
#                 ),
#             }

#         connection = data.get("connection")

#         if not connection:
#             return {
#                 "success": False,
#                 "error": "Django returned no P6 connection details.",
#             }

#         return {
#             "success": True,
#             "connection": connection,
#         }

#     except requests.HTTPError as exc:

#         status_code = (
#             exc.response.status_code
#             if exc.response is not None
#             else None
#         )

#         logger.warning(
#             "Django P6 connection lookup failed | "
#             "connection_id=%s | status=%s",
#             connection_id,
#             status_code,
#         )

#         try:
#             error_data = exc.response.json()
#             message = error_data.get(
#                 "message",
#                 "Unable to retrieve P6 connection.",
#             )
#         except Exception:
#             message = (
#                 "Unable to retrieve the requested P6 connection."
#             )

#         return {
#             "success": False,
#             "error": message,
#         }

#     except requests.RequestException as exc:

#         logger.error(
#             "Django P6 connection request failed: %s",
#             exc,
#         )

#         return {
#             "success": False,
#             "error": (
#                 "Unable to contact the AI Sidekick "
#                 "connection service."
#             ),
#         }

#     except ValueError:

#         return {
#             "success": False,
#             "error": (
#                 "AI Sidekick returned an invalid response "
#                 "while retrieving the P6 connection."
#             ),
#         }

# def get_p6_connection_session(
#     ctx: Context,
#     connection_id: int,
# ) -> dict[str, Any]:

#     # ---------------------------------------------------------
#     # 1. Check session cache
#     # ---------------------------------------------------------

#     existing_session = get_p6_session(
#         ctx,
#         connection_id,
#     )

#     if existing_session:
#         return {
#             "success": True,
#             "session": existing_session,
#             "source": "session_cache",
#         }


#     # ---------------------------------------------------------
#     # 2. Retrieve selected connection from Django
#     # ---------------------------------------------------------

#     result = _get_connection_from_django(
#         connection_id,
#     )

#     if not result["success"]:
#         return result


#     connection = result["connection"]


#     # ---------------------------------------------------------
#     # 3. Generate P6 authentication token
#     # ---------------------------------------------------------

#     auth_token = _generate_auth_token(
#         connection["username"],
#         connection["password"],
#     )


#     # ---------------------------------------------------------
#     # 4. Login to selected P6 environment
#     # ---------------------------------------------------------

#     cookies = _login_auth(
#         auth_token,
#         connection["base_url"],
#         connection["database_name"],
#     )

#     if not cookies:
#         return {
#             "success": False,
#             "error": (
#                 f"Unable to login to P6 connection "
#                 f"'{connection.get('name', connection_id)}'."
#             ),
#         }


#     # ---------------------------------------------------------
#     # 5. Build session
#     # ---------------------------------------------------------

#     session = {
#         "connection_id": connection_id,
#         "name": connection["name"],
#         "base_url": connection["base_url"],
#         "database_name": connection["database_name"],
#         "username": connection["username"],
#         "auth_token": auth_token,
#         "cookies": cookies,
#         "authenticated_at": datetime.utcnow().isoformat(),
#     }


#     # ---------------------------------------------------------
#     # 6. Cache session for this MCP client + connection
#     # ---------------------------------------------------------

#     set_p6_session(
#         ctx,
#         connection_id,
#         session,
#     )


#     return {
#         "success": True,
#         "session": session,
#         "source": "new_login",
#     }