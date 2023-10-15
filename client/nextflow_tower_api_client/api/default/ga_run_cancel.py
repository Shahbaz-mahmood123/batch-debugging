from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.empty_body_request import EmptyBodyRequest
from ...models.run_id import RunId
from ...models.wes_error_response import WesErrorResponse
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    json_body: EmptyBodyRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/ga4gh/wes/v1/runs/{run_id}/cancel".format(
            run_id=run_id,
        ),
        "json": json_json_body,
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
    run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EmptyBodyRequest,
) -> Response[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RunId, WesErrorResponse]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EmptyBodyRequest,
) -> Optional[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RunId, WesErrorResponse]
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EmptyBodyRequest,
) -> Response[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RunId, WesErrorResponse]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EmptyBodyRequest,
) -> Optional[Union[Any, RunId, WesErrorResponse]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RunId, WesErrorResponse]
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
