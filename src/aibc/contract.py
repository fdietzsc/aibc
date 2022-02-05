# pylint: disable=missing-module-docstring
from typing import List

from aibc import async_make_request


async def contract_info(contract_id: str) -> dict:
    """Get contract details, you can use this to prefill your
    order before you submit an order.

    Args:
        contract_id (str): The contract ID you want details for.

    Returns:
        list: A `Contract` resource.
    """

    return await async_make_request(method='get', endpoint=f'/api/iserver/contract/{contract_id}/info')


async def search_futures(symbols: List[str]) -> dict:
    """Returns a list of non-expired future contracts
    for given symbol(s).

    Args:
        symbols (str): List of case-sensitive symbols separated by comma

    Returns:
        list: A collection of `Futures` resource.
    """

    return await async_make_request(method='get', endpoint='/api/trsrv/futures', params={'symbols': ','.join(symbols)})


async def search_symbol(symbol: str, name: str = False, security_type: str = None) -> list:
    """Search by symbol or name.

    Args:
        symbol (str): The symbol to be searched.
        name (bool, optional): Set to `True` if searching by name, `False` if searching by symbol. Defaults to False.
        security_type (str, optional): The security type of the symbol. Defaults to None.

    Returns:
        list: A collection of `Contract` resources.

    Usage:
        >>> await search_symbol(
            symbol='AAPL',
            name='Apple'
        )
    """
    payload = {
        'symbol': symbol,
        'name': name,
        'secType': security_type
    }

    return await async_make_request(method='post', endpoint='/api/iserver/secdef/search', json_payload=payload)


async def search_multiple_contracts(contract_ids: List[int]) -> list:
    """Returns a list of security definitions for the given conids.

    Args:
        contract_ids (List[str]): A list of Contract IDs.

    Returns:
        list: A collection of `Contract` resources.

    Usage:
        >>> await search_multiple_contracts(
            contract_ids=['265598']
        )
    """
    payload = {"conids": contract_ids}

    return await async_make_request(method='post', endpoint='/api/trsrv/secdef', json_payload=payload)
