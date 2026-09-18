from contextvars import ContextVar


current_api_key = ContextVar(
    "current_api_key",
    default=None
)

current_user = ContextVar(
    "current_user",
    default=None
)