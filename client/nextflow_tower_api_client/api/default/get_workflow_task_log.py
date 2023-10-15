from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.workflow_log_response import WorkflowLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    task_id: int,
    *,
    next_: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["next"] = next_

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/workflow/{workflowId}/log/{taskId}".format(
            workflowId=workflow_id,
            taskId=task_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkflowLogResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    task_id: int,
    *,
    client: AuthenticatedClient,
    next_: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Get workflow task logs

     Retrieves the output logs for the workflow task identified by the given `taskId`.

    Args:
        workflow_id (str):
        task_id (int):
        next_ (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        task_id=task_id,
        next_=next_,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    task_id: int,
    *,
    client: AuthenticatedClient,
    next_: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Get workflow task logs

     Retrieves the output logs for the workflow task identified by the given `taskId`.

    Args:
        workflow_id (str):
        task_id (int):
        next_ (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, WorkflowLogResponse]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        task_id=task_id,
        client=client,
        next_=next_,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    task_id: int,
    *,
    client: AuthenticatedClient,
    next_: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Get workflow task logs

     Retrieves the output logs for the workflow task identified by the given `taskId`.

    Args:
        workflow_id (str):
        task_id (int):
        next_ (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        task_id=task_id,
        next_=next_,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    task_id: int,
    *,
    client: AuthenticatedClient,
    next_: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Get workflow task logs

     Retrieves the output logs for the workflow task identified by the given `taskId`.

    Args:
        workflow_id (str):
        task_id (int):
        next_ (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, WorkflowLogResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            task_id=task_id,
            client=client,
            next_=next_,
            workspace_id=workspace_id,
        )
    ).parsed
