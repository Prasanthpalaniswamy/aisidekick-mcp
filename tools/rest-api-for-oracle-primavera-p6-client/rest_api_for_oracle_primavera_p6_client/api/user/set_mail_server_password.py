from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_user_password_response import SetUserPasswordResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_object_id: str,
    new_password: str,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["UserObjectId"] = user_object_id

    params["NewPassword"] = new_password

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/user/setMailServerPassword",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SetUserPasswordResponse | None:
    if response.status_code == 200:
        response_200 = SetUserPasswordResponse.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SetUserPasswordResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_object_id: str,
    new_password: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | SetUserPasswordResponse]:
    """SetMailServerPassword  Operation

     Sets Mail server Password. You must supply the both the UserObjectId and the NewPassword fields when
    you use the SetMailServerPassword operation.

    Args:
        user_object_id (str):
        new_password (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetUserPasswordResponse]
    """

    kwargs = _get_kwargs(
        user_object_id=user_object_id,
        new_password=new_password,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_object_id: str,
    new_password: str,
    auth_token: str | Unset = UNSET,
) -> Any | SetUserPasswordResponse | None:
    """SetMailServerPassword  Operation

     Sets Mail server Password. You must supply the both the UserObjectId and the NewPassword fields when
    you use the SetMailServerPassword operation.

    Args:
        user_object_id (str):
        new_password (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetUserPasswordResponse
    """

    return sync_detailed(
        client=client,
        user_object_id=user_object_id,
        new_password=new_password,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_object_id: str,
    new_password: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | SetUserPasswordResponse]:
    """SetMailServerPassword  Operation

     Sets Mail server Password. You must supply the both the UserObjectId and the NewPassword fields when
    you use the SetMailServerPassword operation.

    Args:
        user_object_id (str):
        new_password (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SetUserPasswordResponse]
    """

    kwargs = _get_kwargs(
        user_object_id=user_object_id,
        new_password=new_password,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_object_id: str,
    new_password: str,
    auth_token: str | Unset = UNSET,
) -> Any | SetUserPasswordResponse | None:
    """SetMailServerPassword  Operation

     Sets Mail server Password. You must supply the both the UserObjectId and the NewPassword fields when
    you use the SetMailServerPassword operation.

    Args:
        user_object_id (str):
        new_password (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SetUserPasswordResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            user_object_id=user_object_id,
            new_password=new_password,
            auth_token=auth_token,
        )
    ).parsed
