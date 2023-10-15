from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.run_id import RunId
from ...models.run_request import RunRequest
from ...models.wes_error_response import WesErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Dict[str, Any]:
    pass

    json_body.to_dict()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/ga4gh/wes/v1/runs",
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RunId, WesErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RunId.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = WesErrorResponse.from_dict(response.json())

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
) -> Response[Union[Any, RunId, WesErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Response[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RunId, WesErrorResponse]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Optional[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RunId, WesErrorResponse]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Response[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RunId, WesErrorResponse]]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Optional[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RunId, WesErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
