# pylint: disable=missing-module-docstring
from typing import Union
from typing import List
from enum import Enum

from aibc import async_make_request


async def snapshot(contract_ids: List[str], since: int = None, fields: list = None) -> dict:
    """Get Market Data for the given conid(s).

    The endpoint will return by default bid, ask, last, change, change pct, close, listing exchange. See response
    fields for a list of available fields that can be request via fields argument. The endpoint /iserver/accounts
    must be called prior to /iserver/marketdata/snapshot. For derivative contracts the endpoint /iserver/secdef/search
    must be called first. First /snapshot endpoint call for given conid will initiate the market data request.
    To receive all available fields the /snapshot endpoint will need to be called several times. To receive streaming
    market data the endpoint /ws can be used. Refer to Streaming WebSocket Data for details.

    Args:
        contract_ids (List[str]): A list of contract Ids.
        since (int): Time period since which updates are required. uses epoch time with milliseconds.
        fields (list): List of fields to be contained in the response.

    Returns:
        dict: A `MarketSnapshot` resource.

    Usage:
        >>> await snapshot(contract_ids=['265598'])
    """

    fields = ','.join(fields) if fields else None
    params = {'conids': ','.join(contract_ids), 'since': since, 'fields': fields}

    return await async_make_request(method='get', endpoint='/api/iserver/marketdata/snapshot', params=params)


async def market_history(contract_id: str, period: str, bar_type: Union[str, Enum] = None, exchange: str = None,
                         outside_regular_trading_hours: bool = True) -> dict:
    """Get historical market Data for given conid, length of data
    is controlled by 'period' and 'bar'.

    Args:
        contract_id (str): A contract Id.
        period (str): Available time period: {1-30}min, {1-8}h, {1-1000}d, {1-792}w, {1-182}m, {1-15}y
        bar_type (Union[str, Enum], optional): The bar type you want the data in. Defaults to None.
        exchange (str, optional): Exchange of the conid. Defaults to None.
        outside_regular_trading_hours (bool, optional): For contracts that support it, will determine if historical
                                                        data includes outside of regular trading hours. Defaults
                                                        to True.

    Returns:
        dict: A collection `Bar` resources.

    Usage:
        >>> await market_history(contract_id=['265598'])
    """
    if isinstance(bar_type, Enum):
        bar_type = bar_type.value

    payload = {
        'conid': contract_id,
        'period': period,
        'bar': bar_type,
        'exchange': exchange,
        'outsideRth': outside_regular_trading_hours
    }
    return await async_make_request(method='get', endpoint='/api/iserver/marketdata/history', params=payload)
