from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_label_request import CreateLabelRequest
from ...models.create_label_response import CreateLabelResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CreateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/labels",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateLabelResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateLabelResponse.from_dict(response.json())

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
) -> Response[Union[Any, CreateLabelResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateLabelResponse, ErrorResponse]]:
    """Create label

     Creates a new label in a user context. Append `?workspaceId` to create the label in a workspace
    context. Resource labels include `resource: true` and a `value`.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLabelResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateLabelResponse, ErrorResponse]]:
    """Create label

     Creates a new label in a user context. Append `?workspaceId` to create the label in a workspace
    context. Resource labels include `resource: true` and a `value`.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateLabelResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateLabelResponse, ErrorResponse]]:
    """Create label

     Creates a new label in a user context. Append `?workspaceId` to create the label in a workspace
    context. Resource labels include `resource: true` and a `value`.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateLabelResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateLabelResponse, ErrorResponse]]:
    """Create label

     Creates a new label in a user context. Append `?workspaceId` to create the label in a workspace
    context. Resource labels include `resource: true` and a `value`.

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateLabelResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
