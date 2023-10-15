from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.describe_pipeline_response import DescribePipelineResponse
from ...models.error_response import ErrorResponse
from ...models.pipeline_query_attribute import PipelineQueryAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_id: int,
    *,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_attributes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(attributes, Unset):
        if attributes is None:
            json_attributes = None
        else:
            json_attributes = []
            for attributes_item_data in attributes:
                attributes_item = attributes_item_data.value

                json_attributes.append(attributes_item)

    params["attributes"] = json_attributes

    params["workspaceId"] = workspace_id

    params["sourceWorkspaceId"] = source_workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/pipelines/{pipelineId}".format(
            pipelineId=pipeline_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DescribePipelineResponse.from_dict(response.json())

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
) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
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
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe pipeline

     Retrieves the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe pipeline

     Retrieves the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePipelineResponse, ErrorResponse]
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
    ).parsed


async def asyncio_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe pipeline

     Retrieves the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe pipeline

     Retrieves the details of the pipeline identified by the given `pipelineId`.

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePipelineResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            attributes=attributes,
            workspace_id=workspace_id,
            source_workspace_id=source_workspace_id,
        )
    ).parsed
