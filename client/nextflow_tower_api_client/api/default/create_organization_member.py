from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_member_request import AddMemberRequest
from ...models.add_member_response import AddMemberResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    org_id: int,
    *,
    json_body: AddMemberRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/orgs/{orgId}/members/add".format(
            orgId=org_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddMemberResponse, Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AddMemberResponse.from_dict(response.json())

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
) -> Response[Union[AddMemberResponse, Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddMemberRequest,
) -> Response[Union[AddMemberResponse, Any, ErrorResponse]]:
    """Add organization member

     Adds a new member to the organization identified by the given `orgId`.

    Args:
        org_id (int):
        json_body (AddMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddMemberResponse, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddMemberRequest,
) -> Optional[Union[AddMemberResponse, Any, ErrorResponse]]:
    """Add organization member

     Adds a new member to the organization identified by the given `orgId`.

    Args:
        org_id (int):
        json_body (AddMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddMemberResponse, Any, ErrorResponse]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddMemberRequest,
) -> Response[Union[AddMemberResponse, Any, ErrorResponse]]:
    """Add organization member

     Adds a new member to the organization identified by the given `orgId`.

    Args:
        org_id (int):
        json_body (AddMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddMemberResponse, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddMemberRequest,
) -> Optional[Union[AddMemberResponse, Any, ErrorResponse]]:
    """Add organization member

     Adds a new member to the organization identified by the given `orgId`.

    Args:
        org_id (int):
        json_body (AddMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddMemberResponse, Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
