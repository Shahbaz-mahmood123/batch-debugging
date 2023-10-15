from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    run_name: Union[Unset, None, str] = UNSET,
    session_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["runName"] = run_name

    params["sessionId"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/workflow/validate",
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
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
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
    *,
    client: AuthenticatedClient,
    run_name: Union[Unset, None, str] = UNSET,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Check that the given run name of a workflow has a valid format. When the session ID is given: check
    that no other workflow in the system exists with the combination of both elements

    Args:
        run_name (Union[Unset, None, str]):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        run_name=run_name,
        session_id=session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    run_name: Union[Unset, None, str] = UNSET,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Check that the given run name of a workflow has a valid format. When the session ID is given: check
    that no other workflow in the system exists with the combination of both elements

    Args:
        run_name (Union[Unset, None, str]):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        run_name=run_name,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    run_name: Union[Unset, None, str] = UNSET,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Check that the given run name of a workflow has a valid format. When the session ID is given: check
    that no other workflow in the system exists with the combination of both elements

    Args:
        run_name (Union[Unset, None, str]):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        run_name=run_name,
        session_id=session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    run_name: Union[Unset, None, str] = UNSET,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Check that the given run name of a workflow has a valid format. When the session ID is given: check
    that no other workflow in the system exists with the combination of both elements

    Args:
        run_name (Union[Unset, None, str]):
        session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            run_name=run_name,
            session_id=session_id,
        )
    ).parsed
