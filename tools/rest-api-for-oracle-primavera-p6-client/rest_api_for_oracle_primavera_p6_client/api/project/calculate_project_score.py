from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calculate_project_score_response import CalculateProjectScoreResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_object_id: str,
    project_code_type_object_id: str,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["ProjectObjectId"] = project_object_id

    params["ProjectCodeTypeObjectId"] = project_code_type_object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/project/calculateProjectScore",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CalculateProjectScoreResponse | None:
    if response.status_code == 200:
        response_200 = CalculateProjectScoreResponse.from_dict(response.json())

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
) -> Response[Any | CalculateProjectScoreResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str,
    project_code_type_object_id: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | CalculateProjectScoreResponse]:
    """Calculate Project Score

     Calculate the project score of a project specified by the ProjectObjectId based on a selected set of
    ProjectCodeTypeObjectId's. The Project Score feature helps you evaluate projects by using project
    codes to identify and quantify characteristics that can be used to determine project rankings. P6
    EPPM Web Services uses the weighted project code and code values assigned to a project to calculate
    its score. To use project scoring features, you create weighted project codes that represent project
    criteria you want to evaluate, for example, projected sales and risk. You further express the
    possible attributes associated with these evaluation criteria as weighted project code values, for
    example, projected sales might be described as either high, medium, or low potential. Finally, you
    assign the appropriate weighted codes and code values to the projects you want to score. Typically,
    project code and code value weights are set up by a project controls or system administrator.

    Args:
        project_object_id (str):
        project_code_type_object_id (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CalculateProjectScoreResponse]
    """

    kwargs = _get_kwargs(
        project_object_id=project_object_id,
        project_code_type_object_id=project_code_type_object_id,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str,
    project_code_type_object_id: str,
    auth_token: str | Unset = UNSET,
) -> Any | CalculateProjectScoreResponse | None:
    """Calculate Project Score

     Calculate the project score of a project specified by the ProjectObjectId based on a selected set of
    ProjectCodeTypeObjectId's. The Project Score feature helps you evaluate projects by using project
    codes to identify and quantify characteristics that can be used to determine project rankings. P6
    EPPM Web Services uses the weighted project code and code values assigned to a project to calculate
    its score. To use project scoring features, you create weighted project codes that represent project
    criteria you want to evaluate, for example, projected sales and risk. You further express the
    possible attributes associated with these evaluation criteria as weighted project code values, for
    example, projected sales might be described as either high, medium, or low potential. Finally, you
    assign the appropriate weighted codes and code values to the projects you want to score. Typically,
    project code and code value weights are set up by a project controls or system administrator.

    Args:
        project_object_id (str):
        project_code_type_object_id (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CalculateProjectScoreResponse
    """

    return sync_detailed(
        client=client,
        project_object_id=project_object_id,
        project_code_type_object_id=project_code_type_object_id,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str,
    project_code_type_object_id: str,
    auth_token: str | Unset = UNSET,
) -> Response[Any | CalculateProjectScoreResponse]:
    """Calculate Project Score

     Calculate the project score of a project specified by the ProjectObjectId based on a selected set of
    ProjectCodeTypeObjectId's. The Project Score feature helps you evaluate projects by using project
    codes to identify and quantify characteristics that can be used to determine project rankings. P6
    EPPM Web Services uses the weighted project code and code values assigned to a project to calculate
    its score. To use project scoring features, you create weighted project codes that represent project
    criteria you want to evaluate, for example, projected sales and risk. You further express the
    possible attributes associated with these evaluation criteria as weighted project code values, for
    example, projected sales might be described as either high, medium, or low potential. Finally, you
    assign the appropriate weighted codes and code values to the projects you want to score. Typically,
    project code and code value weights are set up by a project controls or system administrator.

    Args:
        project_object_id (str):
        project_code_type_object_id (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CalculateProjectScoreResponse]
    """

    kwargs = _get_kwargs(
        project_object_id=project_object_id,
        project_code_type_object_id=project_code_type_object_id,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_object_id: str,
    project_code_type_object_id: str,
    auth_token: str | Unset = UNSET,
) -> Any | CalculateProjectScoreResponse | None:
    """Calculate Project Score

     Calculate the project score of a project specified by the ProjectObjectId based on a selected set of
    ProjectCodeTypeObjectId's. The Project Score feature helps you evaluate projects by using project
    codes to identify and quantify characteristics that can be used to determine project rankings. P6
    EPPM Web Services uses the weighted project code and code values assigned to a project to calculate
    its score. To use project scoring features, you create weighted project codes that represent project
    criteria you want to evaluate, for example, projected sales and risk. You further express the
    possible attributes associated with these evaluation criteria as weighted project code values, for
    example, projected sales might be described as either high, medium, or low potential. Finally, you
    assign the appropriate weighted codes and code values to the projects you want to score. Typically,
    project code and code value weights are set up by a project controls or system administrator.

    Args:
        project_object_id (str):
        project_code_type_object_id (str):
        auth_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CalculateProjectScoreResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_object_id=project_object_id,
            project_code_type_object_id=project_code_type_object_id,
            auth_token=auth_token,
        )
    ).parsed
