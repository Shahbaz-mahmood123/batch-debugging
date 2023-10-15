from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_dataset_request import CreateDatasetRequest
from ...models.create_dataset_response import CreateDatasetResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    workspace_id: int,
    *,
    json_body: CreateDatasetRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/workspaces/{workspaceId}/datasets".format(
            workspaceId=workspace_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateDatasetResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create dataset

     Creates a new Tower dataset in the given workspace context. Include the dataset file and details in
    your request body.

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create dataset

     Creates a new Tower dataset in the given workspace context. Include the dataset file and details in
    your request body.

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateDatasetResponse, ErrorResponse]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create dataset

     Creates a new Tower dataset in the given workspace context. Include the dataset file and details in
    your request body.

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create dataset

     Creates a new Tower dataset in the given workspace context. Include the dataset file and details in
    your request body.

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateDatasetResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
