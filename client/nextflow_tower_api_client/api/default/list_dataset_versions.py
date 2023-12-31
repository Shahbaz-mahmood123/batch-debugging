from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_dataset_versions_response import ListDatasetVersionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: int,
    dataset_id: str,
    *,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["mimeType"] = mime_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/workspaces/{workspaceId}/datasets/{datasetId}/versions".format(
            workspaceId=workspace_id,
            datasetId=dataset_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListDatasetVersionsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all dataset versions

     Lists all versions of the given `datasetId`.

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        mime_type=mime_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all dataset versions

     Lists all versions of the given `datasetId`.

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListDatasetVersionsResponse]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        mime_type=mime_type,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all dataset versions

     Lists all versions of the given `datasetId`.

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        mime_type=mime_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all dataset versions

     Lists all versions of the given `datasetId`.

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse, ListDatasetVersionsResponse]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            dataset_id=dataset_id,
            client=client,
            mime_type=mime_type,
        )
    ).parsed
