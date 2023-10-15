from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.label_type import LabelType
from ...models.list_labels_response import ListLabelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, LabelType] = UNSET,
    is_default: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["max"] = max_

    params["offset"] = offset

    params["search"] = search

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["isDefault"] = is_default

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/labels",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListLabelsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListLabelsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListLabelsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, LabelType] = UNSET,
    is_default: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListLabelsResponse]]:
    """List labels

     Lists all available labels in a user context. Append `?workspaceId` to list labels in a workspace
    context.

    Args:
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        type (Union[Unset, None, LabelType]):
        is_default (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListLabelsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        type=type,
        is_default=is_default,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, LabelType] = UNSET,
    is_default: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListLabelsResponse]]:
    """List labels

     Lists all available labels in a user context. Append `?workspaceId` to list labels in a workspace
    context.

    Args:
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        type (Union[Unset, None, LabelType]):
        is_default (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListLabelsResponse]
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        type=type,
        is_default=is_default,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, LabelType] = UNSET,
    is_default: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListLabelsResponse]]:
    """List labels

     Lists all available labels in a user context. Append `?workspaceId` to list labels in a workspace
    context.

    Args:
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        type (Union[Unset, None, LabelType]):
        is_default (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListLabelsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
        type=type,
        is_default=is_default,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, LabelType] = UNSET,
    is_default: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListLabelsResponse]]:
    """List labels

     Lists all available labels in a user context. Append `?workspaceId` to list labels in a workspace
    context.

    Args:
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):
        type (Union[Unset, None, LabelType]):
        is_default (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListLabelsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            max_=max_,
            offset=offset,
            search=search,
            type=type,
            is_default=is_default,
        )
    ).parsed
