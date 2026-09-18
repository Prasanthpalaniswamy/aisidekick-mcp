from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_resource_response import DocumentResourceResponse
from ...models.upload_document_body import UploadDocumentBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadDocumentBody | Unset = UNSET,
    project_object_id: str,
    activity_object_id: str | Unset = UNSET,
    title: str | Unset = UNSET,
    security_policy: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    document_category_name: str | Unset = UNSET,
    description: str | Unset = UNSET,
    reference_number: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_token, Unset):
        headers["AuthToken"] = auth_token

    params: dict[str, Any] = {}

    params["ProjectObjectId"] = project_object_id

    params["ActivityObjectId"] = activity_object_id

    params["Title"] = title

    params["SecurityPolicy"] = security_policy

    params["Owner"] = owner

    params["DocumentCategoryName"] = document_category_name

    params["Description"] = description

    params["ReferenceNumber"] = reference_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document/uploadDocument",
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
    body: UploadDocumentBody | Unset = UNSET,
    project_object_id: str,
    activity_object_id: str | Unset = UNSET,
    title: str | Unset = UNSET,
    security_policy: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    document_category_name: str | Unset = UNSET,
    description: str | Unset = UNSET,
    reference_number: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | DocumentResourceResponse]:
    """Upload Document

     Upload new document

    Args:
        project_object_id (str):
        activity_object_id (str | Unset):
        title (str | Unset):
        security_policy (str | Unset):
        owner (str | Unset):
        document_category_name (str | Unset):
        description (str | Unset):
        reference_number (str | Unset):
        auth_token (str | Unset):
        body (UploadDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DocumentResourceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        project_object_id=project_object_id,
        activity_object_id=activity_object_id,
        title=title,
        security_policy=security_policy,
        owner=owner,
        document_category_name=document_category_name,
        description=description,
        reference_number=reference_number,
        auth_token=auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentBody | Unset = UNSET,
    project_object_id: str,
    activity_object_id: str | Unset = UNSET,
    title: str | Unset = UNSET,
    security_policy: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    document_category_name: str | Unset = UNSET,
    description: str | Unset = UNSET,
    reference_number: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | DocumentResourceResponse | None:
    """Upload Document

     Upload new document

    Args:
        project_object_id (str):
        activity_object_id (str | Unset):
        title (str | Unset):
        security_policy (str | Unset):
        owner (str | Unset):
        document_category_name (str | Unset):
        description (str | Unset):
        reference_number (str | Unset):
        auth_token (str | Unset):
        body (UploadDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DocumentResourceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        project_object_id=project_object_id,
        activity_object_id=activity_object_id,
        title=title,
        security_policy=security_policy,
        owner=owner,
        document_category_name=document_category_name,
        description=description,
        reference_number=reference_number,
        auth_token=auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentBody | Unset = UNSET,
    project_object_id: str,
    activity_object_id: str | Unset = UNSET,
    title: str | Unset = UNSET,
    security_policy: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    document_category_name: str | Unset = UNSET,
    description: str | Unset = UNSET,
    reference_number: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Response[Any | DocumentResourceResponse]:
    """Upload Document

     Upload new document

    Args:
        project_object_id (str):
        activity_object_id (str | Unset):
        title (str | Unset):
        security_policy (str | Unset):
        owner (str | Unset):
        document_category_name (str | Unset):
        description (str | Unset):
        reference_number (str | Unset):
        auth_token (str | Unset):
        body (UploadDocumentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DocumentResourceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        project_object_id=project_object_id,
        activity_object_id=activity_object_id,
        title=title,
        security_policy=security_policy,
        owner=owner,
        document_category_name=document_category_name,
        description=description,
        reference_number=reference_number,
        auth_token=auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDocumentBody | Unset = UNSET,
    project_object_id: str,
    activity_object_id: str | Unset = UNSET,
    title: str | Unset = UNSET,
    security_policy: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    document_category_name: str | Unset = UNSET,
    description: str | Unset = UNSET,
    reference_number: str | Unset = UNSET,
    auth_token: str | Unset = UNSET,
) -> Any | DocumentResourceResponse | None:
    """Upload Document

     Upload new document

    Args:
        project_object_id (str):
        activity_object_id (str | Unset):
        title (str | Unset):
        security_policy (str | Unset):
        owner (str | Unset):
        document_category_name (str | Unset):
        description (str | Unset):
        reference_number (str | Unset):
        auth_token (str | Unset):
        body (UploadDocumentBody | Unset):

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
            project_object_id=project_object_id,
            activity_object_id=activity_object_id,
            title=title,
            security_policy=security_policy,
            owner=owner,
            document_category_name=document_category_name,
            description=description,
            reference_number=reference_number,
            auth_token=auth_token,
        )
    ).parsed
