from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unit_of_measure import UnitOfMeasure
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    fields: str,
    order_by: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["Filter"] = filter_

    params["Fields"] = fields

    params["OrderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/unitOfMeasure",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[UnitOfMeasure] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UnitOfMeasure.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[UnitOfMeasure]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    fields: str,
    order_by: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[UnitOfMeasure]]:
    """Read UnitOfMeasures

     Reads UnitOfMeasure objects from the database.

    Args:
        filter_ (str | Unset):
        fields (str):
        order_by (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[UnitOfMeasure]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        fields=fields,
        order_by=order_by,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    fields: str,
    order_by: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | list[UnitOfMeasure] | None:
    """Read UnitOfMeasures

     Reads UnitOfMeasure objects from the database.

    Args:
        filter_ (str | Unset):
        fields (str):
        order_by (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[UnitOfMeasure]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        fields=fields,
        order_by=order_by,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    fields: str,
    order_by: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[UnitOfMeasure]]:
    """Read UnitOfMeasures

     Reads UnitOfMeasure objects from the database.

    Args:
        filter_ (str | Unset):
        fields (str):
        order_by (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[UnitOfMeasure]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        fields=fields,
        order_by=order_by,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    fields: str,
    order_by: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | list[UnitOfMeasure] | None:
    """Read UnitOfMeasures

     Reads UnitOfMeasure objects from the database.

    Args:
        filter_ (str | Unset):
        fields (str):
        order_by (str | Unset):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[UnitOfMeasure]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            fields=fields,
            order_by=order_by,
            auth_token=auth_token,
        )
    ).parsed
