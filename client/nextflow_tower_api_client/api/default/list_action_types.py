from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_event_types_response import ListEventTypesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/actions/types",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListEventTypesResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListEventTypesResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListEventTypesResponse]]:
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
) -> Response[Union[Any, ErrorResponse, ListEventTypesResponse]]:
    """List action event types

     Lists the supported event types that trigger a pipeline action. Append `?workspaceId` to list event
    types in a workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListEventTypesResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListEventTypesResponse]]:
    """List action event types

     Lists the supported event types that trigger a pipeline action. Append `?workspaceId` to list event
    types in a workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListEventTypesResponse]
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListEventTypesResponse]]:
    """List action event types

     Lists the supported event types that trigger a pipeline action. Append `?workspaceId` to list event
    types in a workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListEventTypesResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListEventTypesResponse]]:
    """List action event types

     Lists the supported event types that trigger a pipeline action. Append `?workspaceId` to list event
    types in a workspace context.

    Args:
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListEventTypesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
