"""A client library for accessing REST API for Oracle Primavera P6"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
