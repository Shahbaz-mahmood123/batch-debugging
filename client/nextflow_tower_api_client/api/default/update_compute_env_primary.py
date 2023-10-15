from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.empty_body_request import EmptyBodyRequest
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    compute_env_id: str,
    *,
    json_body: EmptyBodyRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/compute-envs/{computeEnvId}/primary".format(
            computeEnvId=compute_env_id,
        ),
        "json": json_json_body,
        "params": params,
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
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EmptyBodyRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Define primary compute environment

     Selects the compute environment identified by the given `computeEnvId` as the primary compute
    environment in the given workspace context.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        compute_env_id=compute_env_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EmptyBodyRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Define primary compute environment

     Selects the compute environment identified by the given `computeEnvId` as the primary compute
    environment in the given workspace context.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        compute_env_id=compute_env_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EmptyBodyRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Define primary compute environment

     Selects the compute environment identified by the given `computeEnvId` as the primary compute
    environment in the given workspace context.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        compute_env_id=compute_env_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    json_body: EmptyBodyRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Define primary compute environment

     Selects the compute environment identified by the given `computeEnvId` as the primary compute
    environment in the given workspace context.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            compute_env_id=compute_env_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
