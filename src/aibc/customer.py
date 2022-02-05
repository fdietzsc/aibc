# pylint: disable=missing-module-docstring
from aibc import async_make_request


async def customer_info() -> dict:
    """Returns Applicant Id with all owner related entities.

    Returns:
        dict: A customer resource object.
    """
    return await async_make_request(method='get', endpoint='/api/ibcust/entity/info')
