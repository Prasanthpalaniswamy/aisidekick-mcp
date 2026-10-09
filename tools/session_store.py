from typing import Any
from mcp.server.fastmcp import Context


UNIFIER_SESSIONS: dict[str, dict[str, Any]] = {}

# session_key
#     └── connection_id
#             └── P6 authentication/session data
P6_SESSIONS: dict[str, dict[int, dict[str, Any]]] = {}


def get_session_key(ctx: Context) -> str:
    if ctx.client_id:
        return f"client:{ctx.client_id}"

    try:
        session = ctx.session
    except Exception:
        session = None

    if session is not None:
        return f"session:{id(session)}"

    return f"request:{ctx.request_id}"


def get_p6_session(
    ctx: Context,
    connection_id: int,
) -> dict[str, Any] | None:

    session_key = get_session_key(ctx)

    return (
        P6_SESSIONS
        .get(session_key, {})
        .get(connection_id)
    )


def set_p6_session(
    ctx: Context,
    connection_id: int,
    session: dict[str, Any],
) -> None:

    session_key = get_session_key(ctx)

    if session_key not in P6_SESSIONS:
        P6_SESSIONS[session_key] = {}

    P6_SESSIONS[session_key][connection_id] = {
        **session,
        "connection_id": connection_id,
    }


def clear_p6_session(
    ctx: Context,
    connection_id: int,
) -> bool:

    session_key = get_session_key(ctx)

    sessions = P6_SESSIONS.get(session_key)

    if not sessions:
        return False

    if connection_id not in sessions:
        return False

    del sessions[connection_id]

    if not sessions:
        del P6_SESSIONS[session_key]

    return True


def clear_all_p6_sessions(
    ctx: Context,
) -> None:

    session_key = get_session_key(ctx)

    P6_SESSIONS.pop(session_key, None)