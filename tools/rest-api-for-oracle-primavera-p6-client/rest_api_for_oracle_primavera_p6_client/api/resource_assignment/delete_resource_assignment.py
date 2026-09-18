from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    object_id: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["ObjectId"] = object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/resourceAssignment",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | bool]:
    """Delete ResourceAssignments

     Send a request to this endpoint to delete one or more resourceAssignment. Objects with ID values
    that match the values provided in the request body will be deleted.

    Args:
        object_id (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | bool | None:
    """Delete ResourceAssignments

     Send a request to this endpoint to delete one or more resourceAssignment. Objects with ID values
    that match the values provided in the request body will be deleted.

    Args:
        object_id (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return sync_detailed(
        client=client,
        object_id=object_id,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | bool]:
    """Delete ResourceAssignments

     Send a request to this endpoint to delete one or more resourceAssignment. Objects with ID values
    that match the values provided in the request body will be deleted.

    Args:
        object_id (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    object_id: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | bool | None:
    """Delete ResourceAssignments

     Send a request to this endpoint to delete one or more resourceAssignment. Objects with ID values
    that match the values provided in the request body will be deleted.

    Args:
        object_id (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return (
        await asyncio_detailed(
            client=client,
            object_id=object_id,
            auth_token=auth_token,
        )
    ).parsed
