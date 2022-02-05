# pylint: disable=missing-module-docstring
from aibc import async_make_request


async def get_trades() -> list:
    """Returns a list of trades for the currently selected
    account for current day and six previous days.

    Returns:
        list: A collection of `Trade` resources.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/account/trades')
