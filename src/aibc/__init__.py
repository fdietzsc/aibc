import urllib3
import aiohttp
from dataclasses import dataclass

from typing import Union
from typing import Tuple
from urllib3.exceptions import InsecureRequestWarning
from fake_useragent import UserAgent
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
    LastPrice: str = '31'
    Symbol: str = '55'
    Text: str = '58'
    High: str = '70'
    Low: str = '71'
    Position: str = '72'
    MarketValue: str = '73'
    AvgPrice: str = '74'
    UnrealizedPnl: str = '75'
    FormattedPosition: str = '76'
    FormattedUnrealizedPnl: str = '77'
    DailyPnl: str = '78'
    Change: str = '82'
    ChangePercent: str = '83'
    BidPrice: str = '84'
    AskSize: str = '85'
    AskPrice: str = '86'
    Volume: str = '87'
    BidSize: str = '88'
    Exchange: str = '6004'
    Conid: str = '6008'
    SecType: str = '6070'
    Months: str = '6072'
    RegularExpiry: str = '6073'
    Marker: str = '6119'
    UnderlyingContract: str = '6457'
    MarketDataAvailability: str = '6509'
    CompanyName: str = '7051'
    AskExch: str = '7057'
    LastExch: str = '7058'
    LastSize: str = '7059'
    BidExch: str = '7068'
    MarketDataAvailabilityOther: str = '7084'
    PutCallInterest: str = '7085'
    PutCallVolume: str = '7086'
    HistoricVolumePercent: str = '7087'
    HistoricVolumeClosePercent: str = '7088'
    OptionVolume: str = '7089'
    ContractIdAndExchange: str = '7094'
    ContractDescription: str = '7219'
    ContractDescriptionOther: str = '7220'
    ListingExchange: str = '7221'
    Industry: str = '7280'
    Category: str = '7281'
    AverageVolume: str = '7282'
    OptionImpliedVolatilityPercent: str = '7283'
    HistoricVolume: str = '7284'
    PutCallRatio: str = '7285'
    DividendAmount: str = '7286'
    DividentYield: str = '7287'
    Ex: str = '7288'
    MarketCap: str = '7289'
    PriceEarningsRatio: str = '7290'
    EarningsPerShare: str = '7291'
    CostBasis: str = '7292'
    FiftyTwoWeekLow: str = '7293'
    FiftyTwoWeekHigh: str = '7294'
    Open: str = '7295'
    Close: str = '7296'
    Delta: str = '7308'
    Gamma: str = '7309'
    Theta: str = '7310'
    Vega: str = '7311'
    OptionVolumeChangePercent: str = '7607'
    ImpliedVolatilityPercent: str = '7633'
    Mark: str = '7635'
    ShortableShares: str = '7636'
    FeeRate: str = '7637'
    OptionOpenInterest: str = '7638'
    PercentOfMarketValue: str = '7639'
    Shortable: str = '7644'
    MorningstarRating: str = '7655'
    Dividends: str = '7671'
    DividendsTtm: str = '7672'
    EMATwoHundred: str = '7674'
    EMAOneHundred: str = '7675'
    EMAFiftyDay: str = '7676'
    EMATwentyDay: str = '7677'
    PriceEMATwoHundredDay: str = '7678'
    PriceEMAOneHundredDay: str = '7679'
    PriceEMAFiftyDay: str = '7680'
    PriceEMATwentyDay: str = '7681'
    ChangeSinceOpen: str = '7682'
    UpcomingEvent: str = '7683'
    UpcomingEventDate: str = '7684'
    UpcomingAnalystMeeting: str = '7685'
    UpcomingEarnings: str = '7686'
    UpcomingMiscEvents: str = '7687'
    RecentAnalystMeeting: str = '7688'
    RecentEarnings: str = '7689'
    RecentMiscEvents: str = '7690'
    ProbabilityOfMaxReturnCustomer: str = '7694'
    BreakEven: str = '7695'
    SpxDelta: str = '7696'
    FuturesOpenInterest: str = '7697'
    LastYield: str = '7698'
    BidYield: str = '7699'
    ProbabilityMaxReturn: str = '7700'
    ProbabilityMaxLoss: str = '7702'
    ProfitProbability: str = '7703'
    OrganizationType: str = '7704'
    DebtClass: str = '7705'
    Ratings: str = '7706'
    BondStateCode: str = '7707'
    BondType: str = '7708'
    LastTradingDate: str = '7714'
    IssueDate: str = '7715'
    Beta: str = '7718'
    AskYield: str = '7720'
    PriorClose: str = '7741'
    VolumeLong: str = '7762'
    All: Tuple[str] = (
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
        >>> BarTypes.OneMinute
    """

    OneMinute: str = '1min'
    TwoMinute: str = '2min'
    ThreeMinute: str = '3min'
    FiveMinute: str = '5min'
    TenMinute: str = '10min'
    FifteenMinute: str = '15min'
    ThirtyMinute: str = '30min'
    OneHour: str = '1h'
    TwoHour: str = '2h'
    ThreeHour: str = '3h'
    FourHour: str = '4h'
    EightHour: str = '8h'
    OneDay: str = '1d'
    OneWeek: str = '1w'
    OneMonth: str = '1m'


@dataclass
class SortDirection:
    """Represents the sort directions for the
    `PortfolioPositions` service.

    ### Usage
    ----
        >>> from aibc import SortDirection
        >>> SortDirection.Ascending
    """

    Ascending: str = 'a'
    Descending: str = 'd'


@dataclass
class SortFields:
    """Represents the sort fields for the
    `PortfolioPositions` service.

    ### Usage
    ----
        >>> from aibc import SortFields
        >>> SortFields.MarketPrice
    """

    AccountId: str = 'acctId'
    ContractId: str = 'conid'
    ContractDescription: str = 'contractDesc'
    Position: str = 'position'
    MarketPrice: str = 'mktPrice'
    MarketValue: str = 'MktValue'
    Currency: str = 'USD'
    AverageCost: str = 'avgCost'
    AveragePrice: str = 'avgPrice'
    RealizedPnl: str = 'realizedPnl'
    UnrealizedPnl: str = 'unrealizedPnl'
    Exchanges: str = 'exchs'
    ExpirationDate: str = 'expiry'
    PutOrCall: str = 'putOrCall'
    Multiplier: str = 'multiplier'
    Strike: str = 'strike'
    ExerciseStyle: str = 'exerciseStyle'
    AssetClass: str = 'assetClass'
    Model: str = 'model'
    UnderlyingContractId: str = 'undConid'
    BaseMarketValue: str = 'baseMktValue'
    BaseMarketPrice: str = 'baseMktPrice'
    BaseAverageCost: str = 'BaseAvgCost'
    BaseAveragePrice: str = 'BaseAvgPrice'
    BaseRealizedPnl: str = 'baseRealizedPnl'
    BaseUnrealizedPnl: str = 'baseUnrealizedPnl'


async def get(session, url: str, headers: dict, params: dict = None, json_payload: dict = None):
    async with session.get(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
        return await handle_response(resp)


async def post(session, url: str, headers: dict, params: dict = None, json_payload: dict = None):
    async with session.post(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
        return await handle_response(resp)


async def delete(session, url: str, headers: dict, params: dict = None, json_payload: dict = None):
    async with session.delete(url, params=params, json=json_payload, headers=headers, ssl=False) as resp:
        return await handle_response(resp)


async def handle_response(response: aiohttp.ClientResponse):
    # If it's okay and no details.
    if response.ok:
        return await response.json()


async def async_make_request(method: str, endpoint: str, params: dict = None,
                             json_payload: dict = None) -> Union[list, dict]:
    """Handles all the requests in the library.

    ### Overview
    ---
    A central function used to handle all the requests made in the library,
    this function handles building the URL, defining Content-Type, passing
    through payloads, and handling any errors that may arise during the
    request.

    ### Parameters
    ----
    method : str
        The Request method, can be one of the following:
        ['get','post','put','delete','patch']

    endpoint : str
        The API URL endpoint, example is 'quotes'

    params : dict (optional, Default={})
        The URL params for the request.

    data : dict (optional, Default={})
    A data payload for a request.

    json_payload : dict (optional, Default={})
        A json data payload for a request

    ### Returns
    ----
    Dict:
        A Dictionary object containing the
        JSON values.
    """

    # Build the URL.
    url = RESOURCE_URL + endpoint
    headers = {"Content-Type": "application/json",
               "User-Agent": UserAgent().ff}

    async with aiohttp.ClientSession() as session:
        if method == 'post':
            response = await post(session, url, headers, params=params, json_payload=json_payload)
        elif method == 'get':
            response = await get(session, url, headers, params=params, json_payload=json_payload)
        elif method == 'delete':
            response = await delete(session, url, headers, params=params, json_payload=json_payload)

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
