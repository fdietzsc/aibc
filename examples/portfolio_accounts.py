import asyncio

from aibc import portfolio


async def async_main():
    print('\nCall of asynchronous method in asynchronous code')
    print('------------------------------------------------')
    print(await portfolio.accounts())


def main():
    print('\nCall of asynchronous method in synchronous code')
    print('-----------------------------------------------')
    print(asyncio.run(portfolio.accounts()))


if __name__ == '__main__':
    main()
    asyncio.run(async_main())
