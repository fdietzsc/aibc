import asyncio
import argparse

from aibc import portfolio


async def async_main(aid: str):
    print('\nCall of asynchronous method in asynchronous code')
    print('------------------------------------------------')
    print(await portfolio.account_summary(aid))


def main(aid: str):
    print('\nCall of asynchronous method in synchronous code')
    print('-----------------------------------------------')
    print(asyncio.run(portfolio.account_summary(aid)))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('account_id', help='Interactive Brokers account ID', type=str)
    args = parser.parse_args()

    main(args.account_id)
    asyncio.run(async_main(args.account_id))
