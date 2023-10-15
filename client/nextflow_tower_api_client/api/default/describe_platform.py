from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.describe_platform_response import DescribePlatformResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    platform_id: str,
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["regionId"] = region_id

    params["credentialsId"] = credentials_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/platforms/{platformId}".format(
            platformId=platform_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DescribePlatformResponse.from_dict(response.json())

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
) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe platform

     Retrieves the details of the computing platform identified by the given `platformId`.

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe platform

     Retrieves the details of the computing platform identified by the given `platformId`.

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePlatformResponse, ErrorResponse]
    """

    return sync_detailed(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
    ).parsed


async def asyncio_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe platform

     Retrieves the details of the computing platform identified by the given `platformId`.

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe platform

     Retrieves the details of the computing platform identified by the given `platformId`.

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribePlatformResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            platform_id=platform_id,
            client=client,
            workspace_id=workspace_id,
            region_id=region_id,
            credentials_id=credentials_id,
        )
    ).parsed
