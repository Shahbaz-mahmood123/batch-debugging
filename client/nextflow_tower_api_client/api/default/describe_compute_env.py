from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compute_env_query_attribute import ComputeEnvQueryAttribute
from ...models.describe_compute_env_response import DescribeComputeEnvResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    compute_env_id: str,
    *,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ComputeEnvQueryAttribute]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    json_attributes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(attributes, Unset):
        if attributes is None:
            json_attributes = None
        else:
            json_attributes = []
            for attributes_item_data in attributes:
                attributes_item = attributes_item_data.value

                json_attributes.append(attributes_item)

    params["attributes"] = json_attributes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/compute-envs/{computeEnvId}".format(
            computeEnvId=compute_env_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DescribeComputeEnvResponse.from_dict(response.json())

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
) -> Response[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
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
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ComputeEnvQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
    """Describe compute environment

     Retrieves the details of the Tower compute environment identified by the given `computeEnvId`.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ComputeEnvQueryAttribute]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        compute_env_id=compute_env_id,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ComputeEnvQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
    """Describe compute environment

     Retrieves the details of the Tower compute environment identified by the given `computeEnvId`.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ComputeEnvQueryAttribute]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribeComputeEnvResponse, ErrorResponse]
    """

    return sync_detailed(
        compute_env_id=compute_env_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    ).parsed


async def asyncio_detailed(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ComputeEnvQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
    """Describe compute environment

     Retrieves the details of the Tower compute environment identified by the given `computeEnvId`.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ComputeEnvQueryAttribute]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        compute_env_id=compute_env_id,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    compute_env_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ComputeEnvQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeComputeEnvResponse, ErrorResponse]]:
    """Describe compute environment

     Retrieves the details of the Tower compute environment identified by the given `computeEnvId`.

    Args:
        compute_env_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ComputeEnvQueryAttribute]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DescribeComputeEnvResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            compute_env_id=compute_env_id,
            client=client,
            workspace_id=workspace_id,
            attributes=attributes,
        )
    ).parsed
