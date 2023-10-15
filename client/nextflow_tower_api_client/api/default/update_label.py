from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_label_request import UpdateLabelRequest
from ...models.update_label_response import UpdateLabelResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    label_id: int,
    *,
    json_body: UpdateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/labels/{labelId}".format(
            labelId=label_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateLabelResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    label_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    """Update label

     Updates the label identified by the given `labelId`.

    Args:
        label_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UpdateLabelResponse]]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    """Update label

     Updates the label identified by the given `labelId`.

    Args:
        label_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UpdateLabelResponse]
    """

    return sync_detailed(
        label_id=label_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    label_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    """Update label

     Updates the label identified by the given `labelId`.

    Args:
        label_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UpdateLabelResponse]]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label_id: int,
    *,
    client: AuthenticatedClient,
    json_body: UpdateLabelRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, UpdateLabelResponse]]:
    """Update label

     Updates the label identified by the given `labelId`.

    Args:
        label_id (int):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, UpdateLabelResponse]
    """

    return (
        await asyncio_detailed(
            label_id=label_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
