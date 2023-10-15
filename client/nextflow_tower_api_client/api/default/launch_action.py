from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.launch_action_request import LaunchActionRequest
from ...models.launch_action_response import LaunchActionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: str,
    *,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/actions/{actionId}/launch".format(
            actionId=action_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LaunchActionResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger Tower Launch action

     Triggers the execution of the Tower Launch action identified by the given `actionId`.

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger Tower Launch action

     Triggers the execution of the Tower Launch action identified by the given `actionId`.

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, LaunchActionResponse]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger Tower Launch action

     Triggers the execution of the Tower Launch action identified by the given `actionId`.

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger Tower Launch action

     Triggers the execution of the Tower Launch action identified by the given `actionId`.

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, LaunchActionResponse]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
