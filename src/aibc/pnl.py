from aibc import async_make_request


async def pnl_server_account() -> dict:
    """Returns an object containing PnL for the selected account
    and its models (if any).

    Returns:
        dict: An `AccountPnL` resource.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/account/pnl/partitioned')
