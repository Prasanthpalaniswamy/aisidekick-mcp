from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.risk_category import RiskCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RiskCategory],
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/riskCategory",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

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
    body: list[RiskCategory],
    auth_token: str | Unset = UNSET,
) -> Response[Any | bool]:
    """Update RiskCategories

     Send a request to this endpoint to update one or more riskCategory. For each JSON object provided in
    the request body, an application object with a matching ID value will be updated to reflect the JSON
    contents.

    Args:
        auth_token (str | Unset):
        body (list[RiskCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list[RiskCategory],
    auth_token: str | Unset = UNSET,
) -> Any | bool | None:
    """Update RiskCategories

     Send a request to this endpoint to update one or more riskCategory. For each JSON object provided in
    the request body, an application object with a matching ID value will be updated to reflect the JSON
    contents.

    Args:
        auth_token (str | Unset):
        body (list[RiskCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return sync_detailed(
        client=client,
        body=body,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RiskCategory],
    auth_token: str | Unset = UNSET,
) -> Response[Any | bool]:
    """Update RiskCategories

     Send a request to this endpoint to update one or more riskCategory. For each JSON object provided in
    the request body, an application object with a matching ID value will be updated to reflect the JSON
    contents.

    Args:
        auth_token (str | Unset):
        body (list[RiskCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[RiskCategory],
    auth_token: str | Unset = UNSET,
) -> Any | bool | None:
    """Update RiskCategories

     Send a request to this endpoint to update one or more riskCategory. For each JSON object provided in
    the request body, an application object with a matching ID value will be updated to reflect the JSON
    contents.

    Args:
        auth_token (str | Unset):
        body (list[RiskCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            auth_token=auth_token,
        )
    ).parsed
