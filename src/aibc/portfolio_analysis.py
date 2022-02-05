from typing import List
from typing import Union

from enum import Enum

from aibc import async_make_request


async def account_performance(account_ids: List[str], frequency: Union[str, Enum]) -> dict:
    """Returns the performance (MTM) for the given accounts, if more than one account
    is passed, the result is consolidated.

    Args:
        account_ids (List[str]): A list of account Numbers.
        frequency (Union[str, Enum]): Frequency of cumulative performance
                                      data points: 'D'aily, 'M'onthly,'Q'uarterly. Can be one of
                                      3 possible values: "D" "M" "Q".

    Returns:
        dict: A performance resource.
    """
    # Grab the Order Status.
    if isinstance(frequency, Enum):
        frequency = frequency.value
    payload = {'acctIds': account_ids, 'freq': frequency}
    return await async_make_request(method='post', endpoint='/api/pa/performance', json_payload=payload)


async def account_summary(account_ids: List[str]) -> dict:
    """Returns a summary of all account balances for the given accounts,
    if more than one account is passed, the result is consolidated.

    Args:
        account_ids (List[str]): A list of account Numbers.

    Returns:
        dict: A performance resource.
    """
    payload = {'acctIds': account_ids}
    return await async_make_request(method='post', endpoint='/api/pa/summary', json_payload=payload)


async def transactions_history(account_ids: List[str] = None, contract_ids: List[str] = None,
                               currency: str = 'USD', days: int = 90) -> dict:
    """Transaction history for a given number of conids and accounts. Types of transactions
    include dividend payments, buy and sell transactions, transfers.

    Args:
        account_ids (List[str]): A list of account Numbers.
        contract_ids (List[str]): A list contract IDs.
        currency (str, optional): The currency for which to return values. Defaults to 'USD'.
        days (int, optional): The number of days to return. Defaults to 90.

    Returns:
        dict : A collection of `Transactions` resource.
    """
    payload = {
        'acctIds': account_ids,
        'conids': contract_ids,
        'currency': currency,
        'days': days
    }
    return await async_make_request(method='post', endpoint='/api/pa/summary', json_payload=payload)
