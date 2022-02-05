from aibc import async_make_request


async def accounts() -> dict:
    """Returns the Users Accounts.

    Returns a list of accounts the user has trading access to,
    their respective aliases and the currently selected account.
    Note this endpoint must be called before modifying an order
    or querying open orders.

    Returns:
        dict: A collection of `Account` resources.

    """
    return await async_make_request(method='get', endpoint='/api/iserver/accounts')


async def pnl_server_account() -> dict:
    """Returns an object containing PnL for the selected account
    and its models (if any).

    Returns:
        dict: An `AccountPnL` resource.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/account/pnl/partitioned')
