from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_tasks_response import ListTasksResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    sort_dir: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["max"] = max_

    params["offset"] = offset

    params["sortBy"] = sort_by

    params["sortDir"] = sort_dir

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/workflow/{workflowId}/tasks".format(
            workflowId=workflow_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListTasksResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListTasksResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListTasksResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    sort_dir: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListTasksResponse]]:
    """List the tasks for the given Workflow ID and filter parameters

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        sort_dir (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTasksResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        sort_by=sort_by,
        sort_dir=sort_dir,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    sort_dir: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListTasksResponse]]:
    """List the tasks for the given Workflow ID and filter parameters

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        sort_dir (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListTasksResponse]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        sort_by=sort_by,
        sort_dir=sort_dir,
        search=search,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    sort_dir: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListTasksResponse]]:
    """List the tasks for the given Workflow ID and filter parameters

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        sort_dir (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTasksResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        sort_by=sort_by,
        sort_dir=sort_dir,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    sort_dir: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListTasksResponse]]:
    """List the tasks for the given Workflow ID and filter parameters

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        sort_dir (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListTasksResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            workspace_id=workspace_id,
            max_=max_,
            offset=offset,
            sort_by=sort_by,
            sort_dir=sort_dir,
            search=search,
        )
    ).parsed
