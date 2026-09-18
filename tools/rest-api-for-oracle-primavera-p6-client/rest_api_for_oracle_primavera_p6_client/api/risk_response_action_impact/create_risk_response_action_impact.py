from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_risk_response_action_impact_response import CreateRiskResponseActionImpactResponse
from ...models.risk_response_action_impact import RiskResponseActionImpact
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RiskResponseActionImpact],
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/riskResponseActionImpact",
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
) -> Any | CreateRiskResponseActionImpactResponse | None:
    if response.status_code == 201:
        response_201 = CreateRiskResponseActionImpactResponse.from_dict(response.json())

        return response_201

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
) -> Response[Any | CreateRiskResponseActionImpactResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RiskResponseActionImpact],
    auth_token: str | Unset = UNSET,
) -> Response[Any | CreateRiskResponseActionImpactResponse]:
    """Create RiskResponseActionImpacts

     Send a request to this endpoint to create one or more riskResponseActionImpact. An application
    object will be created for each JSON object provided in the request body.

    Args:
        auth_token (str | Unset):
        body (list[RiskResponseActionImpact]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateRiskResponseActionImpactResponse]
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
    body: list[RiskResponseActionImpact],
    auth_token: str | Unset = UNSET,
) -> Any | CreateRiskResponseActionImpactResponse | None:
    """Create RiskResponseActionImpacts

     Send a request to this endpoint to create one or more riskResponseActionImpact. An application
    object will be created for each JSON object provided in the request body.

    Args:
        auth_token (str | Unset):
        body (list[RiskResponseActionImpact]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateRiskResponseActionImpactResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RiskResponseActionImpact],
    auth_token: str | Unset = UNSET,
) -> Response[Any | CreateRiskResponseActionImpactResponse]:
    """Create RiskResponseActionImpacts

     Send a request to this endpoint to create one or more riskResponseActionImpact. An application
    object will be created for each JSON object provided in the request body.

    Args:
        auth_token (str | Unset):
        body (list[RiskResponseActionImpact]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateRiskResponseActionImpactResponse]
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
    body: list[RiskResponseActionImpact],
    auth_token: str | Unset = UNSET,
) -> Any | CreateRiskResponseActionImpactResponse | None:
    """Create RiskResponseActionImpacts

     Send a request to this endpoint to create one or more riskResponseActionImpact. An application
    object will be created for each JSON object provided in the request body.

    Args:
        auth_token (str | Unset):
        body (list[RiskResponseActionImpact]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateRiskResponseActionImpactResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            auth_token=auth_token,
        )
    ).parsed
