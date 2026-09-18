from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.read_wbs_role_spread_response import ReadWBSRoleSpreadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    wbs_object_id: str | Unset = UNSET,
    role_object_id: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    include_cumulative: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["WBSObjectId"] = wbs_object_id

    params["RoleObjectId"] = role_object_id

    params["PeriodType"] = period_type

    params["StartDate"] = start_date

    params["EndDate"] = end_date

    params["IncludeCumulative"] = include_cumulative

    params["SpreadField"] = spread_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spread/wbsRoleSpread",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ReadWBSRoleSpreadResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReadWBSRoleSpreadResponse.from_dict(response_200_item_data)

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
) -> Response[Any | list[ReadWBSRoleSpreadResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    wbs_object_id: str | Unset = UNSET,
    role_object_id: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    include_cumulative: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[ReadWBSRoleSpreadResponse]]:
    """ReadWBSRoleSpread

     Reads the spreads of the specified role assignments to the activities from the specified WBS.

    Args:
        wbs_object_id (str | Unset):
        role_object_id (str | Unset):
        period_type (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        include_cumulative (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ReadWBSRoleSpreadResponse]]
    """

    kwargs = _get_kwargs(
        wbs_object_id=wbs_object_id,
        role_object_id=role_object_id,
        period_type=period_type,
        start_date=start_date,
        end_date=end_date,
        include_cumulative=include_cumulative,
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
    wbs_object_id: str | Unset = UNSET,
    role_object_id: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    include_cumulative: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Any | list[ReadWBSRoleSpreadResponse] | None:
    """ReadWBSRoleSpread

     Reads the spreads of the specified role assignments to the activities from the specified WBS.

    Args:
        wbs_object_id (str | Unset):
        role_object_id (str | Unset):
        period_type (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        include_cumulative (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ReadWBSRoleSpreadResponse]
    """

    return sync_detailed(
        client=client,
        wbs_object_id=wbs_object_id,
        role_object_id=role_object_id,
        period_type=period_type,
        start_date=start_date,
        end_date=end_date,
        include_cumulative=include_cumulative,
        spread_field=spread_field,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    wbs_object_id: str | Unset = UNSET,
    role_object_id: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    include_cumulative: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | list[ReadWBSRoleSpreadResponse]]:
    """ReadWBSRoleSpread

     Reads the spreads of the specified role assignments to the activities from the specified WBS.

    Args:
        wbs_object_id (str | Unset):
        role_object_id (str | Unset):
        period_type (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        include_cumulative (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ReadWBSRoleSpreadResponse]]
    """

    kwargs = _get_kwargs(
        wbs_object_id=wbs_object_id,
        role_object_id=role_object_id,
        period_type=period_type,
        start_date=start_date,
        end_date=end_date,
        include_cumulative=include_cumulative,
        spread_field=spread_field,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    wbs_object_id: str | Unset = UNSET,
    role_object_id: str | Unset = UNSET,
    period_type: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    include_cumulative: str | Unset = UNSET,
    spread_field: str,
    auth_token: str | Unset = UNSET,
) -> Any | list[ReadWBSRoleSpreadResponse] | None:
    """ReadWBSRoleSpread

     Reads the spreads of the specified role assignments to the activities from the specified WBS.

    Args:
        wbs_object_id (str | Unset):
        role_object_id (str | Unset):
        period_type (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        include_cumulative (str | Unset):
        spread_field (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ReadWBSRoleSpreadResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            wbs_object_id=wbs_object_id,
            role_object_id=role_object_id,
            period_type=period_type,
            start_date=start_date,
            end_date=end_date,
            include_cumulative=include_cumulative,
            spread_field=spread_field,
            auth_token=auth_token,
        )
    ).parsed
