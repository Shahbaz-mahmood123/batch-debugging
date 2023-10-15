from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_pipeline_secret_request import CreatePipelineSecretRequest
from ...models.create_pipeline_secret_response import CreatePipelineSecretResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CreatePipelineSecretRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/pipeline-secrets",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreatePipelineSecretResponse.from_dict(response.json())

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
) -> Response[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePipelineSecretRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    """Create pipeline secret

     Creates a new pipeline secret in the user context. Append `?workspaceId` to create the secret in a
    workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreatePipelineSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreatePipelineSecretRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    """Create pipeline secret

     Creates a new pipeline secret in the user context. Append `?workspaceId` to create the secret in a
    workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreatePipelineSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePipelineSecretResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePipelineSecretRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    """Create pipeline secret

     Creates a new pipeline secret in the user context. Append `?workspaceId` to create the secret in a
    workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreatePipelineSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreatePipelineSecretRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreatePipelineSecretResponse, ErrorResponse]]:
    """Create pipeline secret

     Creates a new pipeline secret in the user context. Append `?workspaceId` to create the secret in a
    workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreatePipelineSecretRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePipelineSecretResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
