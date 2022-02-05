# pylint: disable=missing-module-docstring
from typing import Union
from typing import Tuple
from dataclasses import dataclass

import aiohttp
from fake_useragent import UserAgent

import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)


RESOURCE_URL = "https://ibgw:5000/v1"


@dataclass
class Frequency:
    """Represents the frequency options for the
    `PortfolioAnalysis` service.

    ### Usage
    ----
        >>> from aibc import Frequency
        >>> Frequency.Daily
    """

    daily: str = 'D'
    monthly: str = 'M'
    quarterly: str = 'Q'


@dataclass
class MarketDataFields:
    """Represents the fields for the
    `MarketDataSnapshot` service.

    ### Usage
    ----
        >>> from aibc import MarketDataFields
        >>> MarketDataFields.Symbol
    """

    # pylint: disable=too-many-instance-attributes
    last_price: str = '31'
    symbol: str = '55'
    text: str = '58'
    high: str = '70'
    low: str = '71'
    position: str = '72'
    market_value: str = '73'
    avg_price: str = '74'
    unrealized_pnl: str = '75'
    formatted_position: str = '76'
    formatted_unrealized_pnl: str = '77'
    daily_pnl: str = '78'
    change: str = '82'
    change_percent: str = '83'
    bid_price: str = '84'
    ask_size: str = '85'
    ask_price: str = '86'
    volume: str = '87'
    bid_size: str = '88'
    exchange: str = '6004'
    conid: str = '6008'
    sec_type: str = '6070'
    months: str = '6072'
    regular_expiry: str = '6073'
    marker: str = '6119'
    underlying_contract: str = '6457'
    market_data_availability: str = '6509'
    company_name: str = '7051'
    ask_exch: str = '7057'
    last_exch: str = '7058'
    last_size: str = '7059'
    bid_exch: str = '7068'
    market_data_availability_other: str = '7084'
    put_call_interest: str = '7085'
    put_call_volume: str = '7086'
    historic_volume_percent: str = '7087'
    historic_volume_close_percent: str = '7088'
    option_volume: str = '7089'
    contract_id_and_exchange: str = '7094'
    contract_description: str = '7219'
    contract_description_other: str = '7220'
    listing_exchange: str = '7221'
    industry: str = '7280'
    category: str = '7281'
    average_volume: str = '7282'
    option_implied_volatility_percent: str = '7283'
    historic_volume: str = '7284'
    put_call_ratio: str = '7285'
    dividend_amount: str = '7286'
    divident_yield: str = '7287'
    ex: str = '7288'
    market_cap: str = '7289'
    price_earnings_ratio: str = '7290'
    earnings_per_share: str = '7291'
    cost_basis: str = '7292'
    fifty_two_week_low: str = '7293'
    fifty_two_week_high: str = '7294'
    open: str = '7295'
    close: str = '7296'
    delta: str = '7308'
    gamma: str = '7309'
    theta: str = '7310'
    vega: str = '7311'
    option_volume_change_percent: str = '7607'
    implied_volatility_percent: str = '7633'
    mark: str = '7635'
    shortable_shares: str = '7636'
    fee_rate: str = '7637'
    option_open_interest: str = '7638'
    percent_of_market_value: str = '7639'
    shortable: str = '7644'
    morningstar_rating: str = '7655'
    dividends: str = '7671'
    dividends_ttm: str = '7672'
    ematwo_hundred: str = '7674'
    emaone_hundred: str = '7675'
    emafifty_day: str = '7676'
    ematwenty_day: str = '7677'
    price_ematwo_hundred_day: str = '7678'
    price_emaone_hundred_day: str = '7679'
    price_emafifty_day: str = '7680'
    price_ematwenty_day: str = '7681'
    change_since_open: str = '7682'
    upcoming_event: str = '7683'
    upcoming_event_date: str = '7684'
    upcoming_analyst_meeting: str = '7685'
    upcoming_earnings: str = '7686'
    upcoming_misc_events: str = '7687'
    recent_analyst_meeting: str = '7688'
    recent_earnings: str = '7689'
    recent_misc_events: str = '7690'
    probability_of_max_return_customer: str = '7694'
    break_even: str = '7695'
    spx_delta: str = '7696'
    futures_open_interest: str = '7697'
    last_yield: str = '7698'
    bid_yield: str = '7699'
    probability_max_return: str = '7700'
    probability_max_loss: str = '7702'
    profit_probability: str = '7703'
    organization_type: str = '7704'
    debt_class: str = '7705'
    ratings: str = '7706'
    bond_state_code: str = '7707'
    bond_type: str = '7708'
    last_trading_date: str = '7714'
    issue_date: str = '7715'
    beta: str = '7718'
    ask_yield: str = '7720'
    prior_close: str = '7741'
    volume_long: str = '7762'
    all: Tuple[str] = (
        '31', '55', '58', '70', '71', '72', '73', '74', '75', '76', '77', '78', '82', '83', '84', '85', '86', '87',
        '88', '6004', '6008', '6070', '6072', '6073', '6119', '6457', '6509', '7051', '7057', '7058', '7059', '7068',
        '7084', '7085', '7086', '7087', '7088', '7089', '7094', '7219', '7220', '7221', '7280', '7281', '7282', '7283',
        '7284', '7285', '7286', '7287', '7288', '7289', '7290', '7291', '7292', '7293', '7294', '7295',
        '7296', '7308', '7309', '7310', '7311', '7607', '7633', '7635', '7636', '7637', '7638', '7639',
        '7644', '7655', '7671', '7672', '7674', '7675', '7676', '7677', '7678', '7679', '7680', '7681',
        '7682', '7683', '7684', '7685', '7686', '7687', '7688', '7689', '7690', '7694', '7695', '7696', '7697',
        '7698', '7699', '7700', '7702', '7703', '7704', '7705', '7706', '7707', '7708', '7714', '7715', '7718',
        '7720', '7741', '7762'
    )


@dataclass
class BarTypes:
    """Represents the bar types for the
    `MarketDataHistory` service.

    ### Usage
    ----
        >>> from aibc import BarTypes
        >>> BarTypes.one_minute
    """

    # pylint: disable=too-many-instance-attributes
    one_minute: str = '1_min'
    two_minute: str = '2_min'
    three_minute: str = '3_min'
    five_minute: str = '5_min'
    ten_minute: str = '10_min'
    fifteen_minute: str = '15_min'
    thirty_minute: str = '30_min'
    one_hour: str = '1_h'
    two_hour: str = '2_h'
    three_hour: str = '3_h'
    four_hour: str = '4_h'
    eight_hour: str = '8_h'
    one_day: str = '1_d'
    one_week: str = '1_w'
    one_month: str = '1_m'


@dataclass
class SortDirection:
    """Represents the sort directions for the
    `PortfolioPositions` service.

    ### Usage
    ----
        >>> from aibc import SortDirection
        >>> SortDirection.Ascending
    """

    ascending: str = 'a'
    descending: str = 'd'


@dataclass
class SortFields:
    """Represents the sort fields for the
    `PortfolioPositions` service.

    ### Usage
    ----
        >>> from aibc import SortFields
        >>> SortFields.MarketPrice
    """

    # pylint: disable=too-many-instance-attributes
    account_id: str = 'acct_id'
    contract_id: str = 'conid'
    contract_description: str = 'contract_desc'
    position: str = 'position'
    market_price: str = 'mkt_price'
    market_value: str = 'mkt_value'
    currency: str = 'usd'
    average_cost: str = 'avg_cost'
    average_price: str = 'avg_price'
    realized_pnl: str = 'realized_pnl'
    unrealized_pnl: str = 'unrealized_pnl'
    exchanges: str = 'exchs'
    expiration_date: str = 'expiry'
    put_or_call: str = 'put_or_call'
    multiplier: str = 'multiplier'
    strike: str = 'strike'
    exercise_style: str = 'exercise_style'
    asset_class: str = 'asset_class'
    model: str = 'model'
    underlying_contract_id: str = 'und_conid'
    base_market_value: str = 'base_mkt_value'
    base_market_price: str = 'base_mkt_price'
    base_average_cost: str = 'base_avg_cost'
    base_average_price: str = 'base_avg_price'
    base_realized_pnl: str = 'base_realized_pnl'
    base_unrealized_pnl: str = 'base_unrealized_pnl'


async def handle_response(response: aiohttp.ClientResponse):
    """Handle response received by aiohttp requests

    Args:
        response (aiohttp.ClientResponse): Response object return by an aiohttp request.

    Returns:
        dict: Containing the JSON values.

    """
    if response.ok:
        return await response.json()


async def async_make_request(method: str, endpoint: str, params: dict = None,
                             json_payload: dict = None) -> Union[list, dict]:
    """Handles all the requests in the library.

    A central function used to handle all the requests made in the library,
    this function handles building the URL, defining Content-Type, passing
    through payloads, and handling any errors that may arise during the
    request.

    Parameters:
        method (str): The Request method, can be one of the following: ['get','post','put','delete','patch']
        endpoint (str): The API URL endpoint, example is 'quotes'
        params (dict, optional): The URL params for the request. Defaults to an empty dict.
        json_payload (dict, optional):  json data payload for a request. Defaults to an empty dict.

    Returns:
        Union[list, dict]: Object containing the JSON response.
    """

    url = RESOURCE_URL + endpoint
    headers = {"Content-Type": "application/json",
               "User-Agent": UserAgent().ff}

    async with aiohttp.ClientSession() as session:
        if method == 'post':
            async with session.post(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
                response = await handle_response(resp)
        elif method == 'get':
            async with session.get(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
                response = await handle_response(resp)
        elif method == 'delete':
            async with session.delete(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
                response = await handle_response(resp)

    return response

    # # If it's okay and no details.
    # if response.ok and len(response.content) > 0:
    #
    #     return response.json()
    #
    # elif len(response.content) > 0 and response.ok:
    #
    #     return {'message': 'response successful',
    #             'status_code': response.status_code
    #             }
    #
    # elif not response.ok and endpoint =='/api/iserver/account':
    #     return response.json()
    #
    # elif not response.ok:
    #
    #     if len(response.content) == 0:
    #         response_data = ''
    #     else:
    #         try:
    #             response_data = response.json()
    #         except:
    #             response_data = {'content': response.text}
    #
    #     # Define the error dict.
    #     error_dict = {'error_code': response.status_code,
    #                   'response_url': response.url,
    #                   'response_body': response_data,
    #                   'response_request': dict(response.request.headers),
    #                   'response_method': response.request.method,
    #                   }
    #
    #     # Log the error.
    #     logging.error(msg=json.dumps(obj=error_dict, indent=4))
    #
    #     raise requests.HTTPError()
