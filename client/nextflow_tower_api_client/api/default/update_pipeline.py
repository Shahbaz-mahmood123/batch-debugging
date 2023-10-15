from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_pipeline_request import UpdatePipelineRequest
from ...models.update_pipeline_response import UpdatePipelineResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_id: int,
    *,
    json_body: UpdatePipelineRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/pipelines/{pipelineId}".format(
            pipelineId=pipeline_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdatePipelineResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdatePipelineRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    """Update pipeline

     Updates the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdatePipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UpdatePipelineResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdatePipelineRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    """Update pipeline

     Updates the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdatePipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UpdatePipelineResponse]
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdatePipelineRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    """Update pipeline

     Updates the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdatePipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UpdatePipelineResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdatePipelineRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UpdatePipelineResponse]]:
    """Update pipeline

     Updates the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdatePipelineRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UpdatePipelineResponse]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
