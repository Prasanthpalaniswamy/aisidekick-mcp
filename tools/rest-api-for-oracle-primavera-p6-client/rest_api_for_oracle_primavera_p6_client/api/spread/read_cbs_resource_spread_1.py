from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.read_cbs_expense_spread_response import ReadCBSExpenseSpreadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_object_id: str | Unset = UNSET,
    baseline_ids: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["ProjectObjectId"] = project_object_id

    params["BaselineIds"] = baseline_ids

    params["PeriodType"] = period_type

    params["SpreadField"] = spread_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spread/cbsExpenseSpread",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ReadCBSExpenseSpreadResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReadCBSExpenseSpreadResponse.from_dict(response_200_item_data)

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
) -> Response[Any | list[ReadCBSExpenseSpreadResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str | Unset = UNSET,
    baseline_ids: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[ReadCBSExpenseSpreadResponse]]:
    """ReadCBSExpenseSpread

     Reads the summarized CBS spreads of the specified project resources

    Args:
        project_object_id (str | Unset):
        baseline_ids (str | Unset):
        period_type (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ReadCBSExpenseSpreadResponse]]
    """

    kwargs = _get_kwargs(
        project_object_id=project_object_id,
        baseline_ids=baseline_ids,
        period_type=period_type,
        spread_field=spread_field,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str | Unset = UNSET,
    baseline_ids: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Any | list[ReadCBSExpenseSpreadResponse] | None:
    """ReadCBSExpenseSpread

     Reads the summarized CBS spreads of the specified project resources

    Args:
        project_object_id (str | Unset):
        baseline_ids (str | Unset):
        period_type (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ReadCBSExpenseSpreadResponse]
    """

    return sync_detailed(
        client=client,
        project_object_id=project_object_id,
        baseline_ids=baseline_ids,
        period_type=period_type,
        spread_field=spread_field,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str | Unset = UNSET,
    baseline_ids: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[ReadCBSExpenseSpreadResponse]]:
    """ReadCBSExpenseSpread

     Reads the summarized CBS spreads of the specified project resources

    Args:
        project_object_id (str | Unset):
        baseline_ids (str | Unset):
        period_type (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ReadCBSExpenseSpreadResponse]]
    """

    kwargs = _get_kwargs(
        project_object_id=project_object_id,
        baseline_ids=baseline_ids,
        period_type=period_type,
        spread_field=spread_field,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str | Unset = UNSET,
    baseline_ids: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Any | list[ReadCBSExpenseSpreadResponse] | None:
    """ReadCBSExpenseSpread

     Reads the summarized CBS spreads of the specified project resources

    Args:
        project_object_id (str | Unset):
        baseline_ids (str | Unset):
        period_type (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ReadCBSExpenseSpreadResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_object_id=project_object_id,
            baseline_ids=baseline_ids,
            period_type=period_type,
            spread_field=spread_field,
            auth_token=auth_token,
        )
    ).parsed
