from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    avatar_id: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/avatars/{avatarId}".format(
            avatarId=avatar_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorResponse, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        avatar_id=avatar_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return sync_detailed(
        avatar_id=avatar_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        avatar_id=avatar_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, File]
    """

    return (
        await asyncio_detailed(
            avatar_id=avatar_id,
            client=client,
        )
    ).parsed
