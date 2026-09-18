from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_period_actual import ActivityPeriodActual
from ...models.create_project_resource_quantity_response import CreateProjectResourceQuantityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[ActivityPeriodActual],
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/activityPeriodActual",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[CreateProjectResourceQuantityResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateProjectResourceQuantityResponse.from_dict(response_200_item_data)

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
) -> Response[Any | list[CreateProjectResourceQuantityResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[ActivityPeriodActual],
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[CreateProjectResourceQuantityResponse]]:
    """Update ActivityPeriodActuals

     Send a request to this endpoint to update one or more ActivityPeriodActuals. An application object
    will be created for each JSON object provided in the request body

    Args:
        auth_token (str | Unset):
        body (list[ActivityPeriodActual]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CreateProjectResourceQuantityResponse]]
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
    body: list[ActivityPeriodActual],
    auth_token: str | Unset = UNSET,
) -> Any | list[CreateProjectResourceQuantityResponse] | None:
    """Update ActivityPeriodActuals

     Send a request to this endpoint to update one or more ActivityPeriodActuals. An application object
    will be created for each JSON object provided in the request body

    Args:
        auth_token (str | Unset):
        body (list[ActivityPeriodActual]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CreateProjectResourceQuantityResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[ActivityPeriodActual],
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[CreateProjectResourceQuantityResponse]]:
    """Update ActivityPeriodActuals

     Send a request to this endpoint to update one or more ActivityPeriodActuals. An application object
    will be created for each JSON object provided in the request body

    Args:
        auth_token (str | Unset):
        body (list[ActivityPeriodActual]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CreateProjectResourceQuantityResponse]]
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
    body: list[ActivityPeriodActual],
    auth_token: str | Unset = UNSET,
) -> Any | list[CreateProjectResourceQuantityResponse] | None:
    """Update ActivityPeriodActuals

     Send a request to this endpoint to update one or more ActivityPeriodActuals. An application object
    will be created for each JSON object provided in the request body

    Args:
        auth_token (str | Unset):
        body (list[ActivityPeriodActual]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CreateProjectResourceQuantityResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            auth_token=auth_token,
        )
    ).parsed
