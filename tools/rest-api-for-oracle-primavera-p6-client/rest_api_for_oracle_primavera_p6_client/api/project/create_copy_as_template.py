from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_copy_as_template import CreateCopyAsTemplate
from ...models.create_copy_as_template_response import CreateCopyAsTemplateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateCopyAsTemplate,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/project/createCopyAsTemplate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateCopyAsTemplateResponse | None:
    if response.status_code == 201:
        response_201 = CreateCopyAsTemplateResponse.from_dict(response.json())

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
) -> Response[Any | CreateCopyAsTemplateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCopyAsTemplate,
    auth_token: str | Unset = UNSET,
) -> Response[Any | CreateCopyAsTemplateResponse]:
    """Create copy as Template

     Creates a copy of the project specified by the ObjectId and makes the copy into a template project.
    The new template project will reside in the EPS node specified by the EPSObjectId.

    Args:
        auth_token (str | Unset):
        body (CreateCopyAsTemplate): CreateCopyAsTemplate Entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCopyAsTemplateResponse]
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
    body: CreateCopyAsTemplate,
    auth_token: str | Unset = UNSET,
) -> Any | CreateCopyAsTemplateResponse | None:
    """Create copy as Template

     Creates a copy of the project specified by the ObjectId and makes the copy into a template project.
    The new template project will reside in the EPS node specified by the EPSObjectId.

    Args:
        auth_token (str | Unset):
        body (CreateCopyAsTemplate): CreateCopyAsTemplate Entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCopyAsTemplateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCopyAsTemplate,
    auth_token: str | Unset = UNSET,
) -> Response[Any | CreateCopyAsTemplateResponse]:
    """Create copy as Template

     Creates a copy of the project specified by the ObjectId and makes the copy into a template project.
    The new template project will reside in the EPS node specified by the EPSObjectId.

    Args:
        auth_token (str | Unset):
        body (CreateCopyAsTemplate): CreateCopyAsTemplate Entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateCopyAsTemplateResponse]
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
    body: CreateCopyAsTemplate,
    auth_token: str | Unset = UNSET,
) -> Any | CreateCopyAsTemplateResponse | None:
    """Create copy as Template

     Creates a copy of the project specified by the ObjectId and makes the copy into a template project.
    The new template project will reside in the EPS node specified by the EPSObjectId.

    Args:
        auth_token (str | Unset):
        body (CreateCopyAsTemplate): CreateCopyAsTemplate Entity

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateCopyAsTemplateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            auth_token=auth_token,
        )
    ).parsed
