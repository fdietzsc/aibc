# pylint: disable=missing-module-docstring
from aibc import async_make_request


async def portfolio_news() -> dict:
    """Returns a news summary for your portfolio.

    Returns:
        list: A collection of `NewsArticle` resources.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/news/portfolio')


async def top_news() -> dict:
    """Returns the top news articles.

    Returns:
        list: A collection of `NewsArticle` resources.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/news/top')


async def news_sources() -> dict:
    """Returns news sources.

    Returns:
        list: A collection of `Sources` resources.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/news/top')


async def news_briefings() -> dict:
    """Returns news briefings.

    Returns:
        list: A collection of `Briefings` resources.
    """
    return await async_make_request(method='get', endpoint='/api/iserver/news/briefing')


async def summary(contract_id: str) -> dict:
    """Returns a summary of the contract ID, items include
    company description and more.

    Args:
        contract_id (str): The contract Id you want to query.

    Returns:
        list: A collection of `Summary` resources.
    """
    return await async_make_request(method='get', endpoint=f'/api/iserver/fundamentals/{contract_id}/summary')
