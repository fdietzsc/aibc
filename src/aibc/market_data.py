from typing import Union
from typing import List
from enum import Enum

from aibc import async_make_request


# TODO: Documentation is outdated
async def snapshot(contract_ids: List[str], since: int = None, fields: Union[str, Enum] = None) -> dict:
    """Get Market Data for the given conid(s).

    The end-point will return by default bid, ask,  last, change, change pct, close,
    listing exchange. The endpoint /iserver/accounts should be called prior to
    /iserver/marketdata/snapshot. To receive all available fields the /snapshot
    endpoint will need to be called several times.

    Args:
        contract_ids (List[str]): A list of contract Ids.

        frequency (Union[str, Enum]): Frequency of cumulative performance data points:
                                      'D'aily, 'M'onthly,'Q'uarterly. Can be one of 3 possible values: "D" "M" "Q".

    Returns:
        dict: A `MarketSnapshot` resource.

    Usage:
        >>> await snapshot(contract_ids=['265598'])
    """

    new_fields = []

    if fields:
        # Check for Enums.
        for field in fields:

            if isinstance(field, Enum):
                field = field.value
            new_fields.append(field)

        fields = ','.join(new_fields)
    else:
        fields = None

    # Define the payload.
    params = {'conids': ','.join(contract_ids), 'since': since, 'fields': fields}

    return await async_make_request(method='get', endpoint='/api/iserver/marketdata/snapshot', params=params)


async def market_history(contract_id: str, period: str, bar: Union[str, Enum] = None, exchange: str = None,
                         outside_regular_trading_hours: bool = True) -> dict:
    """Get historical market Data for given conid, length of data
    is controlled by 'period' and 'bar'.

    Args:
        contract_id (str): A contract Id.
        period (str): Available time period: {1-30}min, {1-8}h, {1-1000}d, {1-792}w, {1-182}m, {1-15}y
        bar (Union[str, Enum], optional): The bar type you want the data in. Defaults to None.
        exchange (str, optional): Exchange of the conid. Defaults to None.
        outside_regular_trading_hours (bool, optional): For contracts that support it, will determine if historical
                                                        data includes outside of regular trading hours. Defaults
                                                        to True.

    Returns:
        dict: A collection `Bar` resources.

    Usage:
        >>> await market_history(contract_id=['265598'])
    """
    if isinstance(bar, Enum):
        bar = bar.value

    payload = {
        'conid': contract_id,
        'period': period,
        'bar': bar,
        'exchange': exchange,
        'outsideRth': outside_regular_trading_hours
    }
    return await async_make_request(method='get', endpoint='/api/iserver/marketdata/history', params=payload)
