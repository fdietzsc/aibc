from aibc import async_make_request


async def scanners() -> dict:
    """Returns an object contains four lists contain all parameters
    for scanners.

    Returns:
        celery.chain: Task chain returning `Scanner` resources
    """
    return await async_make_request(method='get', endpoint='/api/iserver/scanner/params')


async def run_scanner(scanner: dict) -> dict:
    """Runs scanner to get a list of contracts.

    Args:
        scanner (dict): A scanner definition that you want to run.

    Returns:
        celery.chain: Task chain returning collection of `contract` resources

    Usage:
        >>> await run_scanner(
            scanner={
                "instrument": "STK",
                "type": "NOT_YET_TRADED_TODAY",
                "filter": [
                    {
                        "code": "priceAbove",
                        "value": 50
                    },
                    {
                        "code": "priceBelow",
                        "value": 70
                    },
                    {
                        "code": "volumeAbove",
                        "value": None
                    },
                    {
                        "code": "volumeBelow",
                        "value": None
                    }
                ],
                "location": "STK.US.MAJOR",
                "size": "25"
            }
        )
    """
    return await async_make_request(method='post', endpoint='/api/iserver/scanner/run', json_payload=scanner)
