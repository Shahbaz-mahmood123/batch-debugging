from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_participants_response import ListParticipantsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: int,
    workspace_id: int,
    *,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["max"] = max_

    params["offset"] = offset

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/orgs/{orgId}/workspaces/{workspaceId}/participants".format(
            orgId=org_id,
            workspaceId=workspace_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListParticipantsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    """List workspace participants

     Lists the participants of the workspace identified by the given `workspaceId`.

    Args:
        org_id (int):
        workspace_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListParticipantsResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    """List workspace participants

     Lists the participants of the workspace identified by the given `workspaceId`.

    Args:
        org_id (int):
        workspace_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListParticipantsResponse]
    """

    return sync_detailed(
        org_id=org_id,
        workspace_id=workspace_id,
        client=client,
        max_=max_,
        offset=offset,
        search=search,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    """List workspace participants

     Lists the participants of the workspace identified by the given `workspaceId`.

    Args:
        org_id (int):
        workspace_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListParticipantsResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
        max_=max_,
        offset=offset,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListParticipantsResponse]]:
    """List workspace participants

     Lists the participants of the workspace identified by the given `workspaceId`.

    Args:
        org_id (int):
        workspace_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListParticipantsResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            workspace_id=workspace_id,
            client=client,
            max_=max_,
            offset=offset,
            search=search,
        )
    ).parsed
