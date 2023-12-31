from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_participant_role_request import UpdateParticipantRoleRequest
from ...types import Response


def _get_kwargs(
    org_id: int,
    workspace_id: int,
    participant_id: int,
    *,
    json_body: UpdateParticipantRoleRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/orgs/{orgId}/workspaces/{workspaceId}/participants/{participantId}/role".format(
            orgId=org_id,
            workspaceId=workspace_id,
            participantId=participant_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: int,
    workspace_id: int,
    participant_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateParticipantRoleRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Update participant role

     Updates the role of the given participant in the given workspace.

    Args:
        org_id (int):
        workspace_id (int):
        participant_id (int):
        json_body (UpdateParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
        participant_id=participant_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: int,
    workspace_id: int,
    participant_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateParticipantRoleRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update participant role

     Updates the role of the given participant in the given workspace.

    Args:
        org_id (int):
        workspace_id (int):
        participant_id (int):
        json_body (UpdateParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        org_id=org_id,
        workspace_id=workspace_id,
        participant_id=participant_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    workspace_id: int,
    participant_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateParticipantRoleRequest,
) -> Response[Union[Any, ErrorResponse]]:
    """Update participant role

     Updates the role of the given participant in the given workspace.

    Args:
        org_id (int):
        workspace_id (int):
        participant_id (int):
        json_body (UpdateParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
        participant_id=participant_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: int,
    workspace_id: int,
    participant_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateParticipantRoleRequest,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update participant role

     Updates the role of the given participant in the given workspace.

    Args:
        org_id (int):
        workspace_id (int):
        participant_id (int):
        json_body (UpdateParticipantRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            workspace_id=workspace_id,
            participant_id=participant_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
