from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.describe_credentials_response import DescribeCredentialsResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    credentials_id: str,
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/credentials/{credentialsId}".format(
            credentialsId=credentials_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DescribeCredentialsResponse.from_dict(response.json())

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
) -> Response[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    """Describe credentials

     Retrieves the details of the credentials identified by the given `credentialsId`.

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribeCredentialsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        credentials_id=credentials_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    """Describe credentials

     Retrieves the details of the credentials identified by the given `credentialsId`.

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribeCredentialsResponse, ErrorResponse]
    """

    return sync_detailed(
        credentials_id=credentials_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    """Describe credentials

     Retrieves the details of the credentials identified by the given `credentialsId`.

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribeCredentialsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        credentials_id=credentials_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribeCredentialsResponse, ErrorResponse]]:
    """Describe credentials

     Retrieves the details of the credentials identified by the given `credentialsId`.

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribeCredentialsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            credentials_id=credentials_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
