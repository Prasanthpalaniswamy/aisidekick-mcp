from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkin_document_body import CheckinDocumentBody
from ...models.document_resource_response import DocumentResourceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CheckinDocumentBody | Unset = UNSET,
    document_object_id: str,
    project_object_id: str | Unset = UNSET,
    comments: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["DocumentObjectId"] = document_object_id

    params["ProjectObjectId"] = project_object_id

    params["Comments"] = comments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document/checkinDocument",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DocumentResourceResponse | None:
    if response.status_code == 200:
        response_200 = DocumentResourceResponse.from_dict(response.json())

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
) -> Response[Any | DocumentResourceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckinDocumentBody | Unset = UNSET,
    document_object_id: str,
    project_object_id: str | Unset = UNSET,
    comments: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | DocumentResourceResponse]:
    """Checkin Document

     checkin new document to the checkout document

    Args:
        document_object_id (str):
        project_object_id (str | Unset):
        comments (str | Unset):
        auth_token (str | Unset):
        body (CheckinDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DocumentResourceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        document_object_id=document_object_id,
        project_object_id=project_object_id,
        comments=comments,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CheckinDocumentBody | Unset = UNSET,
    document_object_id: str,
    project_object_id: str | Unset = UNSET,
    comments: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | DocumentResourceResponse | None:
    """Checkin Document

     checkin new document to the checkout document

    Args:
        document_object_id (str):
        project_object_id (str | Unset):
        comments (str | Unset):
        auth_token (str | Unset):
        body (CheckinDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DocumentResourceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        document_object_id=document_object_id,
        project_object_id=project_object_id,
        comments=comments,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CheckinDocumentBody | Unset = UNSET,
    document_object_id: str,
    project_object_id: str | Unset = UNSET,
    comments: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | DocumentResourceResponse]:
    """Checkin Document

     checkin new document to the checkout document

    Args:
        document_object_id (str):
        project_object_id (str | Unset):
        comments (str | Unset):
        auth_token (str | Unset):
        body (CheckinDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DocumentResourceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        document_object_id=document_object_id,
        project_object_id=project_object_id,
        comments=comments,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CheckinDocumentBody | Unset = UNSET,
    document_object_id: str,
    project_object_id: str | Unset = UNSET,
    comments: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | DocumentResourceResponse | None:
    """Checkin Document

     checkin new document to the checkout document

    Args:
        document_object_id (str):
        project_object_id (str | Unset):
        comments (str | Unset):
        auth_token (str | Unset):
        body (CheckinDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DocumentResourceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            document_object_id=document_object_id,
            project_object_id=project_object_id,
            comments=comments,
            auth_token=auth_token,
        )
    ).parsed
