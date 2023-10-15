from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_pipelines_response import ListPipelinesResponse
from ...models.pipeline_query_attribute import PipelineQueryAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    visibility: Union[Unset, None, str] = UNSET,
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

    params["max"] = max_

    params["offset"] = offset

    params["search"] = search

    params["visibility"] = visibility

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/pipelines",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListPipelinesResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    visibility: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    """List Tower pipelines

     Lists all available Tower pipelines in a user context. Append `?workspaceId` to list pipelines in a
    workspace context.

    Args:
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        visibility (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListPipelinesResponse]]
    """

    kwargs = _get_kwargs(
        attributes=attributes,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        visibility=visibility,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    visibility: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    """List Tower pipelines

     Lists all available Tower pipelines in a user context. Append `?workspaceId` to list pipelines in a
    workspace context.

    Args:
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        visibility (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListPipelinesResponse]
    """

    return sync_detailed(
        client=client,
        attributes=attributes,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        visibility=visibility,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    visibility: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    """List Tower pipelines

     Lists all available Tower pipelines in a user context. Append `?workspaceId` to list pipelines in a
    workspace context.

    Args:
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        visibility (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListPipelinesResponse]]
    """

    kwargs = _get_kwargs(
        attributes=attributes,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        visibility=visibility,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    visibility: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListPipelinesResponse]]:
    """List Tower pipelines

     Lists all available Tower pipelines in a user context. Append `?workspaceId` to list pipelines in a
    workspace context.

    Args:
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        visibility (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListPipelinesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            attributes=attributes,
            workspace_id=workspace_id,
            max_=max_,
            offset=offset,
            search=search,
            visibility=visibility,
        )
    ).parsed
