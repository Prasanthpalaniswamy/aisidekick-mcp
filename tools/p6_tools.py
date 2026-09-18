import base64
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any
import requests
from mcp.server.fastmcp import Context, FastMCP
from tools.session_store import P6_SESSIONS, get_session_key
from tools.tool_registry import (
    register_tracked_tool
)

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT_SECONDS = 30
EXPORT_OUTPUT_DIR = Path(__file__).resolve().parent / "p6_exported_projects"

def _resolve_credentials(ctx: Context) -> tuple[dict[str, str], list[str]]:
    """Resolve credentials from the current client session first, then environment."""
    mapping = {
        "username": "P6_USERNAME",
        "password": "P6_PASSWORD",
        "base_url": "P6_BASE_URL",
        "database_name": "P6_DATABASE_NAME",
    }

    resolved: dict[str, str] = {}
    missing: list[str] = []

    for key, env_key in mapping.items():
        value = P6_SESSIONS.get(get_session_key(ctx), {}).get(key) or os.environ.get(env_key)
        if value:
            resolved[key] = value
        else:
            missing.append(key)

    return resolved, missing


def _generate_auth_token(username: str, password: str) -> str:
    credentials = f"{username}:{password}"
    return base64.b64encode(credentials.encode("utf-8")).decode("utf-8")


def _create_headers(auth_token: str) -> dict[str, str]:
    return {"AuthToken": auth_token}


def _login_auth(auth_token: str, base_url: str, database_name: str) -> requests.cookies.RequestsCookieJar | None:
    url = f"{base_url.rstrip('/')}/login"
    headers = _create_headers(auth_token)

    try:
        response = requests.post(
            url,
            headers=headers,
            params={"DatabaseName": database_name},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return response.cookies
    except requests.RequestException as exc:
        logger.error("P6 login failed: %s", exc)
        return None


def _get_p6_projects(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    project_filter: str | None = None,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/project"
    headers = _create_headers(auth_token)
    params: dict[str, str] = {
        "Fields": "Name,ObjectId,WBSObjectId,Status",
    }

    if project_filter:
        escaped_project_filter = project_filter.replace("'", "''")
        params["Filter"] = f"Name in ('{escaped_project_filter}')"

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        projects = response.json()
        project_names = [project.get("Name") for project in projects if isinstance(project, dict) and project.get("Name")]
        return {
            "success": True,
            "count": len(projects) if isinstance(projects, list) else None,
            "project_names": project_names,
            "projects": projects,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch projects: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch projects: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 project response was not valid JSON.",
        }


def _get_p6_activities(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/activity"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        activities = response.json()
        return {
            "success": True,
            "count": len(activities) if isinstance(activities, list) else None,
            "activities": activities,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch activities: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch activities: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 activity response was not valid JSON.",
        }


def _get_p6_eps(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/eps"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        eps_items = response.json()
        return {
            "success": True,
            "count": len(eps_items) if isinstance(eps_items, list) else None,
            "eps": eps_items,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch EPS: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch EPS: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 EPS response was not valid JSON.",
        }


def _get_p6_resources(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/resource"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        resources = response.json()
        return {
            "success": True,
            "count": len(resources) if isinstance(resources, list) else None,
            "resources": resources,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch resources: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch resources: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 resource response was not valid JSON.",
        }


def _get_p6_resource_assignments(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/resourceAssignment"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        assignments = response.json()
        return {
            "success": True,
            "count": len(assignments) if isinstance(assignments, list) else None,
            "resource_assignments": assignments,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch resource assignments: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch resource assignments: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 resourceAssignment response was not valid JSON.",
        }


def _get_p6_user_obs(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/userOBS"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        user_obs = response.json()
        return {
            "success": True,
            "count": len(user_obs) if isinstance(user_obs, list) else None,
            "user_obs": user_obs,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch UserOBS: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch UserOBS: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 UserOBS response was not valid JSON.",
        }


def _get_p6_calendars(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/calendar"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        calendars = response.json()
        return {
            "success": True,
            "count": len(calendars) if isinstance(calendars, list) else None,
            "calendars": calendars,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch calendars: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch calendars: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 calendar response was not valid JSON.",
        }


def _get_p6_currencies(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/currency"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        currencies = response.json()
        return {
            "success": True,
            "count": len(currencies) if isinstance(currencies, list) else None,
            "currencies": currencies,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch currencies: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch currencies: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 currency response was not valid JSON.",
        }


def _get_p6_cbss(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    fields: str,
    filter_condition: str,
    order_by: str,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/cbs"
    headers = _create_headers(auth_token)

    try:
        response = requests.get(
            url,
            headers=headers,
            cookies=cookies,
            params={
                "Fields": fields,
                "Filter": filter_condition,
                "OrderBy": order_by,
            },
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        cbss = response.json()
        return {
            "success": True,
            "count": len(cbss) if isinstance(cbss, list) else None,
            "cbss": cbss,
        }
    except requests.RequestException as exc:
        logger.error("Failed to fetch CBSs: %s", exc)
        return {
            "success": False,
            "error": f"Failed to fetch CBSs: {exc}",
        }
    except ValueError:
        return {
            "success": False,
            "error": "P6 CBS response was not valid JSON.",
        }


def _create_p6_eps(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    eps_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/eps"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=eps_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_eps": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create EPS: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create EPS: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create EPS: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create EPS: {exc}",
        }


def _create_p6_resources(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    resource_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/resource"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=resource_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_resources": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create resources: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create resources: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create resources: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create resources: {exc}",
        }


def _create_p6_user_obs(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    user_obs_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/userOBS"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=user_obs_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_user_obs": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create UserOBS: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create UserOBS: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create UserOBS: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create UserOBS: {exc}",
        }


def _create_p6_projects(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    project_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/project"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=project_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_projects": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create projects: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create projects: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create projects: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create projects: {exc}",
        }


def _create_p6_wbs(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    wbs_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/wbs"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=wbs_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_wbs": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create WBS: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create WBS: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create WBS: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create WBS: {exc}",
        }


def _create_p6_activities(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    activity_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/activity"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=activity_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_activities": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create activities: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create activities: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create activities: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create activities: {exc}",
        }


def _create_p6_resource_assignments(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    resource_assignment_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/resourceAssignment"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=resource_assignment_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_resource_assignments": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create resource assignments: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create resource assignments: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create resource assignments: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create resource assignments: {exc}",
        }


def _create_p6_resource_curves(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    resource_curve_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/resourceCurve"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=resource_curve_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_resource_curves": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create resource curves: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create resource curves: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create resource curves: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create resource curves: {exc}",
        }


def _create_p6_risks(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    risk_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/risk"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=risk_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_risks": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create risks: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create risks: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create risks: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create risks: {exc}",
        }


def _create_p6_activity_notes(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    activity_note_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/activityNote"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=activity_note_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_activity_notes": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create activity notes: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create activity notes: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create activity notes: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create activity notes: {exc}",
        }


def _create_p6_activity_steps(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    activity_step_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/activityStep"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=activity_step_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_activity_steps": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create activity steps: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create activity steps: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create activity steps: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create activity steps: {exc}",
        }


def _create_p6_calendars(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    calendar_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/calendar"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=calendar_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_calendars": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create calendars: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create calendars: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create calendars: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create calendars: {exc}",
        }


def _create_p6_currencies(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    currency_list_payload: list[dict[str, Any]],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/currency"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=currency_list_payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        return {
            "success": True,
            "status_code": response.status_code,
            "created_currencies": response.json() if response.text else [],
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to create currencies: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to create currencies: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to create currencies: %s", exc)
        return {
            "success": False,
            "error": f"Failed to create currencies: {exc}",
        }


def _export_p6_project(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/export/exportProject"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type.lower():
            result_data: Any = response.json()
        else:
            result_data = response.text

        return {
            "success": True,
            "status_code": response.status_code,
            "export_result": result_data,
        }
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to export project: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to export project: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to export project: %s", exc)
        return {
            "success": False,
            "error": f"Failed to export project: {exc}",
        }


def _export_p6_projects(
    auth_token: str,
    cookies: requests.cookies.RequestsCookieJar,
    base_url: str,
    payload: dict[str, Any],
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/export/exportProjects"
    headers = {
        **_create_headers(auth_token),
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            cookies=cookies,
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type.lower():
            result_data: Any = response.json()
            saved_file = None
        else:
            result_data = response.text
            EXPORT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"export_projects_{timestamp}.xml"
            file_path = EXPORT_OUTPUT_DIR / filename
            file_path.write_text(result_data, encoding="utf-8")
            saved_file = str(file_path)

        result = {
            "success": True,
            "status_code": response.status_code,
            "export_result": result_data,
        }
        if saved_file:
            result["saved_file"] = saved_file
        return result
    except requests.HTTPError as exc:
        response_text = exc.response.text[:2000] if exc.response is not None and exc.response.text else ""
        logger.error("Failed to export projects: %s | response: %s", exc, response_text)
        return {
            "success": False,
            "error": f"Failed to export projects: {exc}",
            "response_text": response_text,
        }
    except requests.RequestException as exc:
        logger.error("Failed to export projects: %s", exc)
        return {
            "success": False,
            "error": f"Failed to export projects: {exc}",
        }


def _normalize_line_separator(value: str) -> str:
    """Map friendly values to API-accepted line separator strings."""
    normalized = value.strip().upper()
    if normalized == "WINDOWS":
        return "WINDOWS"
    if normalized == "UNIX":
        return "UNIX"
    return value


def register_p6_tools(mcp: FastMCP) -> None:
    @register_tracked_tool(
        mcp
    )
    def set_p6_credentials(
        ctx: Context,
        username: str,
        password: str,
        base_url: str,
        database_name: str,
    ) -> dict[str, Any]:
        """Set P6 credentials for the current client session."""
        P6_SESSIONS[get_session_key(ctx)] = {
            "username": username,
            "password": password,
            "base_url": base_url,
            "database_name": database_name,
        }
        return {
            "success": True,
            "message": "P6 credentials saved for this client session.",
            "source": "session",
        }

    @register_tracked_tool(
        mcp
    )
    def get_p6_credentials_status(ctx: Context) -> dict[str, Any]:
        """Check if required P6 credentials are available from session or environment."""
        _, missing = _resolve_credentials(ctx)
        return {
            "success": len(missing) == 0,
            "missing": missing,
            "has_session_credentials": bool(P6_SESSIONS.get(get_session_key(ctx))),
        }

    @register_tracked_tool(
        mcp
    )
    def clear_p6_session(ctx: Context) -> dict[str, Any]:
        """Clear stored P6 credentials for the current client session."""
        session_key = get_session_key(ctx)
        if session_key in P6_SESSIONS:
            del P6_SESSIONS[session_key]
            return {"success": True, "message": "P6 session cleared."}
        return {"success": True, "message": "No active P6 session found."}

    @register_tracked_tool(
        mcp
    )
    def get_project_from_p6(ctx: Context, project_filter: str = "") -> dict[str, Any]:
        """Get project details from Oracle Primavera P6. Leave project_filter empty to list all projects."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_projects(auth_token, cookies, creds["base_url"], project_filter or None)

    @register_tracked_tool(
        mcp
    )
    def get_activities_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read activities from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_activities(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def get_eps_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read EPS from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_eps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def get_resources_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read resources from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_resources(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def get_resource_assignments_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read resource assignments from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_resource_assignments(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def export_project_from_p6(
        ctx: Context,
        project_object_id: int,
        file_type: str = "XML",
        encoding: str = "UTF-8",
        line_separator: str = "",
        spread_period_type: str = "DAY",
        spacing: str = "  ",
    ) -> dict[str, Any]:
        """Export a P6 project using POST /export/exportProject."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        payload: dict[str, Any] = {
            "ProjectObjectId": project_object_id,
            "FileType": file_type,
            "Encoding": encoding,
            "SpreadPeriodType": spread_period_type,
            "Spacing": spacing,
        }
        if line_separator.strip():
            payload["LineSeparator"] = _normalize_line_separator(line_separator)

        return _export_p6_project(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            payload=payload,
        )

    @register_tracked_tool(
        mcp
    )
    def export_projects_from_p6(
        ctx: Context,
        project_object_ids: str,
        file_type: str = "XML",
        encoding: str = "UTF-8",
        line_separator: str = "",
        spread_period_type: str = "DAY",
        spacing: str = "  ",
    ) -> dict[str, Any]:
        """Export one or more P6 projects using POST /export/exportProjects.

        project_object_ids: comma-separated list of ProjectObjectId values, e.g. "388,389".
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        parsed_ids: list[int] = []
        try:
            parsed_ids = [int(item.strip()) for item in project_object_ids.split(",") if item.strip()]
        except ValueError:
            return {
                "success": False,
                "error": "project_object_ids must be a comma-separated list of integers.",
            }

        if not parsed_ids:
            return {
                "success": False,
                "error": "At least one project_object_id is required.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        payload: dict[str, Any] = {
            "ProjectObjectId": parsed_ids,
            "FileType": file_type,
            "Encoding": encoding,
            "SpreadPeriodType": spread_period_type,
            "Spacing": spacing,
        }
        if line_separator.strip():
            payload["LineSeparator"] = _normalize_line_separator(line_separator)

        return _export_p6_projects(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            payload=payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_eps_in_p6(ctx: Context, eps_items_json: str) -> dict[str, Any]:
        """Create one or more EPS records in P6 using POST /eps.

        Pass a JSON array string of EPS objects as `eps_items_json`.
        Example: '[{"Id":"EPS-1001","Name":"My EPS"}]'
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(eps_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"eps_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "eps_items_json must be a JSON array of EPS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "eps_items_json must contain at least one EPS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in eps_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_eps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            eps_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_resources_in_p6(ctx: Context, resource_items_json: str) -> dict[str, Any]:
        """Create one or more resources in P6 using POST /resource.

        Pass a JSON array string of Resource objects as `resource_items_json`.
        Example: '[{"Id":"RSC-1001","Name":"Sample Resource","ResourceType":"Labor"}]'
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_items_json must be a JSON array of Resource objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_items_json must contain at least one Resource object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resources(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def get_user_obs_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read UserOBS from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_user_obs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def create_user_obs_in_p6(ctx: Context, user_obs_items_json: str) -> dict[str, Any]:
        """Create one or more UserOBS records in P6 using POST /userOBS.

        Pass a JSON array string of UserOBS objects as `user_obs_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(user_obs_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"user_obs_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "user_obs_items_json must be a JSON array of UserOBS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "user_obs_items_json must contain at least one UserOBS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in user_obs_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_user_obs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            user_obs_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_projects_in_p6(ctx: Context, project_items_json: str) -> dict[str, Any]:
        """Create one or more Project records in P6 using POST /project.

        Pass a JSON array string of Project objects as `project_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(project_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"project_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "project_items_json must be a JSON array of Project objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "project_items_json must contain at least one Project object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in project_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_projects(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            project_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_wbs_in_p6(ctx: Context, wbs_items_json: str) -> dict[str, Any]:
        """Create one or more WBS records in P6 using POST /wbs.

        Pass a JSON array string of WBS objects as `wbs_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(wbs_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"wbs_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "wbs_items_json must be a JSON array of WBS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "wbs_items_json must contain at least one WBS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in wbs_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_wbs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            wbs_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_activities_in_p6(ctx: Context, activity_items_json: str) -> dict[str, Any]:
        """Create one or more Activity records in P6 using POST /activity.

        Pass a JSON array string of Activity objects as `activity_items_json`.
        Each activity should include at least `ProjectObjectId` and `WBSObjectId`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_items_json must be a JSON array of Activity objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_items_json must contain at least one Activity object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_items_json must be a JSON object.",
            }

        missing_required = [
            index for index, item in enumerate(parsed_payload)
            if "ProjectObjectId" not in item or "WBSObjectId" not in item
        ]
        if missing_required:
            return {
                "success": False,
                "error": "Each Activity object must include ProjectObjectId and WBSObjectId.",
                "invalid_item_indexes": missing_required,
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activities(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_resource_assignments_in_p6(ctx: Context, resource_assignment_items_json: str) -> dict[str, Any]:
        """Create one or more ResourceAssignment records in P6 using POST /resourceAssignment.

        Pass a JSON array string of ResourceAssignment objects as `resource_assignment_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_assignment_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_assignment_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_assignment_items_json must be a JSON array of ResourceAssignment objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_assignment_items_json must contain at least one ResourceAssignment object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_assignment_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resource_assignments(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_assignment_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_resource_curves_in_p6(ctx: Context, resource_curve_items_json: str) -> dict[str, Any]:
        """Create one or more ResourceCurve records in P6 using POST /resourceCurve.

        Pass a JSON array string of ResourceCurve objects as `resource_curve_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_curve_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_curve_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_curve_items_json must be a JSON array of ResourceCurve objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_curve_items_json must contain at least one ResourceCurve object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_curve_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resource_curves(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_curve_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_risks_in_p6(ctx: Context, risk_items_json: str) -> dict[str, Any]:
        """Create one or more Risk records in P6 using POST /risk.

        Pass a JSON array string of Risk objects as `risk_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(risk_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"risk_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "risk_items_json must be a JSON array of Risk objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "risk_items_json must contain at least one Risk object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in risk_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_risks(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            risk_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_activity_notes_in_p6(ctx: Context, activity_note_items_json: str) -> dict[str, Any]:
        """Create one or more ActivityNote records in P6 using POST /activityNote.

        Pass a JSON array string of ActivityNote objects as `activity_note_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_note_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_note_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_note_items_json must be a JSON array of ActivityNote objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_note_items_json must contain at least one ActivityNote object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_note_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activity_notes(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_note_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_activity_steps_in_p6(ctx: Context, activity_step_items_json: str) -> dict[str, Any]:
        """Create one or more ActivityStep records in P6 using POST /activityStep.

        Pass a JSON array string of ActivityStep objects as `activity_step_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_step_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_step_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_step_items_json must be a JSON array of ActivityStep objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_step_items_json must contain at least one ActivityStep object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_step_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activity_steps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_step_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def create_calendars_in_p6(ctx: Context, calendar_items_json: str) -> dict[str, Any]:
        """Create one or more Calendar records in P6 using POST /calendar.

        Pass a JSON array string of Calendar objects as `calendar_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(calendar_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"calendar_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "calendar_items_json must be a JSON array of Calendar objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "calendar_items_json must contain at least one Calendar object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in calendar_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_calendars(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            calendar_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def get_calendars_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read calendars from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_calendars(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def create_currencies_in_p6(ctx: Context, currency_items_json: str) -> dict[str, Any]:
        """Create one or more Currency records in P6 using POST /currency.

        Pass a JSON array string of Currency objects as `currency_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(currency_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"currency_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "currency_items_json must be a JSON array of Currency objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "currency_items_json must contain at least one Currency object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in currency_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_currencies(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            currency_list_payload=parsed_payload,
        )

    @register_tracked_tool(
        mcp
    )
    def get_currencies_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read currencies from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_currencies(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @register_tracked_tool(
        mcp
    )
    def get_cbss_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read CBS objects from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_cbss(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )


# // Remove after testing the authenticated flow
def register_tools_NOTAUTHENTICATED(mcp: FastMCP) -> None:
    @mcp.tool()
    def set_p6_credentials(
        ctx: Context,
        username: str,
        password: str,
        base_url: str,
        database_name: str,
    ) -> dict[str, Any]:
        """Set P6 credentials for the current client session."""
        P6_SESSIONS[get_session_key(ctx)] = {
            "username": username,
            "password": password,
            "base_url": base_url,
            "database_name": database_name,
        }
        return {
            "success": True,
            "message": "P6 credentials saved for this client session.",
            "source": "session",
        }

    @mcp.tool()
    def get_p6_credentials_status(ctx: Context) -> dict[str, Any]:
        """Check if required P6 credentials are available from session or environment."""
        _, missing = _resolve_credentials(ctx)
        return {
            "success": len(missing) == 0,
            "missing": missing,
            "has_session_credentials": bool(P6_SESSIONS.get(get_session_key(ctx))),
        }

    @mcp.tool()
    def clear_p6_session(ctx: Context) -> dict[str, Any]:
        """Clear stored P6 credentials for the current client session."""
        session_key = get_session_key(ctx)
        if session_key in P6_SESSIONS:
            del P6_SESSIONS[session_key]
            return {"success": True, "message": "P6 session cleared."}
        return {"success": True, "message": "No active P6 session found."}

    @mcp.tool()
    def get_project_from_p6(ctx: Context, project_filter: str = "") -> dict[str, Any]:
        """Get project details from Oracle Primavera P6. Leave project_filter empty to list all projects."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_projects(auth_token, cookies, creds["base_url"], project_filter or None)

    @mcp.tool()
    def get_activities_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read activities from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_activities(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def get_eps_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read EPS from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_eps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def get_resources_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read resources from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_resources(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def get_resource_assignments_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read resource assignments from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_resource_assignments(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def export_project_from_p6(
        ctx: Context,
        project_object_id: int,
        file_type: str = "XML",
        encoding: str = "UTF-8",
        line_separator: str = "",
        spread_period_type: str = "DAY",
        spacing: str = "  ",
    ) -> dict[str, Any]:
        """Export a P6 project using POST /export/exportProject."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        payload: dict[str, Any] = {
            "ProjectObjectId": project_object_id,
            "FileType": file_type,
            "Encoding": encoding,
            "SpreadPeriodType": spread_period_type,
            "Spacing": spacing,
        }
        if line_separator.strip():
            payload["LineSeparator"] = _normalize_line_separator(line_separator)

        return _export_p6_project(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            payload=payload,
        )

    @mcp.tool()
    def export_projects_from_p6(
        ctx: Context,
        project_object_ids: str,
        file_type: str = "XML",
        encoding: str = "UTF-8",
        line_separator: str = "",
        spread_period_type: str = "DAY",
        spacing: str = "  ",
    ) -> dict[str, Any]:
        """Export one or more P6 projects using POST /export/exportProjects.

        project_object_ids: comma-separated list of ProjectObjectId values, e.g. "388,389".
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        parsed_ids: list[int] = []
        try:
            parsed_ids = [int(item.strip()) for item in project_object_ids.split(",") if item.strip()]
        except ValueError:
            return {
                "success": False,
                "error": "project_object_ids must be a comma-separated list of integers.",
            }

        if not parsed_ids:
            return {
                "success": False,
                "error": "At least one project_object_id is required.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        payload: dict[str, Any] = {
            "ProjectObjectId": parsed_ids,
            "FileType": file_type,
            "Encoding": encoding,
            "SpreadPeriodType": spread_period_type,
            "Spacing": spacing,
        }
        if line_separator.strip():
            payload["LineSeparator"] = _normalize_line_separator(line_separator)

        return _export_p6_projects(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            payload=payload,
        )

    @mcp.tool()
    def create_eps_in_p6(ctx: Context, eps_items_json: str) -> dict[str, Any]:
        """Create one or more EPS records in P6 using POST /eps.

        Pass a JSON array string of EPS objects as `eps_items_json`.
        Example: '[{"Id":"EPS-1001","Name":"My EPS"}]'
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(eps_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"eps_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "eps_items_json must be a JSON array of EPS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "eps_items_json must contain at least one EPS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in eps_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_eps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            eps_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_resources_in_p6(ctx: Context, resource_items_json: str) -> dict[str, Any]:
        """Create one or more resources in P6 using POST /resource.

        Pass a JSON array string of Resource objects as `resource_items_json`.
        Example: '[{"Id":"RSC-1001","Name":"Sample Resource","ResourceType":"Labor"}]'
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_items_json must be a JSON array of Resource objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_items_json must contain at least one Resource object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resources(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_list_payload=parsed_payload,
        )

    @mcp.tool()
    def get_user_obs_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read UserOBS from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_user_obs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def create_user_obs_in_p6(ctx: Context, user_obs_items_json: str) -> dict[str, Any]:
        """Create one or more UserOBS records in P6 using POST /userOBS.

        Pass a JSON array string of UserOBS objects as `user_obs_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(user_obs_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"user_obs_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "user_obs_items_json must be a JSON array of UserOBS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "user_obs_items_json must contain at least one UserOBS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in user_obs_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_user_obs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            user_obs_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_projects_in_p6(ctx: Context, project_items_json: str) -> dict[str, Any]:
        """Create one or more Project records in P6 using POST /project.

        Pass a JSON array string of Project objects as `project_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(project_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"project_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "project_items_json must be a JSON array of Project objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "project_items_json must contain at least one Project object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in project_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_projects(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            project_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_wbs_in_p6(ctx: Context, wbs_items_json: str) -> dict[str, Any]:
        """Create one or more WBS records in P6 using POST /wbs.

        Pass a JSON array string of WBS objects as `wbs_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(wbs_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"wbs_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "wbs_items_json must be a JSON array of WBS objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "wbs_items_json must contain at least one WBS object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in wbs_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_wbs(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            wbs_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_activities_in_p6(ctx: Context, activity_items_json: str) -> dict[str, Any]:
        """Create one or more Activity records in P6 using POST /activity.

        Pass a JSON array string of Activity objects as `activity_items_json`.
        Each activity should include at least `ProjectObjectId` and `WBSObjectId`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_items_json must be a JSON array of Activity objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_items_json must contain at least one Activity object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_items_json must be a JSON object.",
            }

        missing_required = [
            index for index, item in enumerate(parsed_payload)
            if "ProjectObjectId" not in item or "WBSObjectId" not in item
        ]
        if missing_required:
            return {
                "success": False,
                "error": "Each Activity object must include ProjectObjectId and WBSObjectId.",
                "invalid_item_indexes": missing_required,
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activities(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_resource_assignments_in_p6(ctx: Context, resource_assignment_items_json: str) -> dict[str, Any]:
        """Create one or more ResourceAssignment records in P6 using POST /resourceAssignment.

        Pass a JSON array string of ResourceAssignment objects as `resource_assignment_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_assignment_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_assignment_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_assignment_items_json must be a JSON array of ResourceAssignment objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_assignment_items_json must contain at least one ResourceAssignment object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_assignment_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resource_assignments(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_assignment_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_resource_curves_in_p6(ctx: Context, resource_curve_items_json: str) -> dict[str, Any]:
        """Create one or more ResourceCurve records in P6 using POST /resourceCurve.

        Pass a JSON array string of ResourceCurve objects as `resource_curve_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(resource_curve_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"resource_curve_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "resource_curve_items_json must be a JSON array of ResourceCurve objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "resource_curve_items_json must contain at least one ResourceCurve object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in resource_curve_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_resource_curves(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            resource_curve_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_risks_in_p6(ctx: Context, risk_items_json: str) -> dict[str, Any]:
        """Create one or more Risk records in P6 using POST /risk.

        Pass a JSON array string of Risk objects as `risk_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(risk_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"risk_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "risk_items_json must be a JSON array of Risk objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "risk_items_json must contain at least one Risk object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in risk_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_risks(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            risk_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_activity_notes_in_p6(ctx: Context, activity_note_items_json: str) -> dict[str, Any]:
        """Create one or more ActivityNote records in P6 using POST /activityNote.

        Pass a JSON array string of ActivityNote objects as `activity_note_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_note_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_note_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_note_items_json must be a JSON array of ActivityNote objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_note_items_json must contain at least one ActivityNote object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_note_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activity_notes(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_note_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_activity_steps_in_p6(ctx: Context, activity_step_items_json: str) -> dict[str, Any]:
        """Create one or more ActivityStep records in P6 using POST /activityStep.

        Pass a JSON array string of ActivityStep objects as `activity_step_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(activity_step_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"activity_step_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "activity_step_items_json must be a JSON array of ActivityStep objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "activity_step_items_json must contain at least one ActivityStep object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in activity_step_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_activity_steps(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            activity_step_list_payload=parsed_payload,
        )

    @mcp.tool()
    def create_calendars_in_p6(ctx: Context, calendar_items_json: str) -> dict[str, Any]:
        """Create one or more Calendar records in P6 using POST /calendar.

        Pass a JSON array string of Calendar objects as `calendar_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(calendar_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"calendar_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "calendar_items_json must be a JSON array of Calendar objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "calendar_items_json must contain at least one Calendar object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in calendar_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_calendars(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            calendar_list_payload=parsed_payload,
        )

    @mcp.tool()
    def get_calendars_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read calendars from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_calendars(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def create_currencies_in_p6(ctx: Context, currency_items_json: str) -> dict[str, Any]:
        """Create one or more Currency records in P6 using POST /currency.

        Pass a JSON array string of Currency objects as `currency_items_json`.
        """
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        try:
            parsed_payload = json.loads(currency_items_json)
        except json.JSONDecodeError as exc:
            return {
                "success": False,
                "error": f"currency_items_json is not valid JSON: {exc}",
            }

        if not isinstance(parsed_payload, list):
            return {
                "success": False,
                "error": "currency_items_json must be a JSON array of Currency objects.",
            }
        if not parsed_payload:
            return {
                "success": False,
                "error": "currency_items_json must contain at least one Currency object.",
            }
        if not all(isinstance(item, dict) for item in parsed_payload):
            return {
                "success": False,
                "error": "Each item in currency_items_json must be a JSON object.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _create_p6_currencies(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            currency_list_payload=parsed_payload,
        )

    @mcp.tool()
    def get_currencies_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read currencies from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_currencies(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )

    @mcp.tool()
    def get_cbss_from_p6(
        ctx: Context,
        fields: str,
        filter_condition: str,
        order_by: str,
    ) -> dict[str, Any]:
        """Read CBS objects from Oracle Primavera P6 using required Fields, Filter, and OrderBy query parameters."""
        creds, missing = _resolve_credentials(ctx)
        if missing:
            return {
                "success": False,
                "requires_credentials": True,
                "missing": missing,
                "error": "P6 credentials are missing. Provide them via set_p6_credentials(...) or environment variables.",
            }

        auth_token = _generate_auth_token(creds["username"], creds["password"])
        cookies = _login_auth(auth_token, creds["base_url"], creds["database_name"])

        if not cookies:
            return {
                "success": False,
                "error": "P6 login failed.",
            }

        return _get_p6_cbss(
            auth_token=auth_token,
            cookies=cookies,
            base_url=creds["base_url"],
            fields=fields,
            filter_condition=filter_condition,
            order_by=order_by,
        )
