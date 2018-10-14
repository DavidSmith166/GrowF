import datetime
from datetime import date, datetime
import warnings
from yahoo_fin.stock_info import *
from yahoo_fin import stock_info


def get_current_stock_value(ticker):
    warnings.simplefilter('ignore')
    stock_value = round(stock_info.get_live_price(ticker), 2)
    return (ticker, datetime.now(), stock_value)


def get_past_date(days_from_current):
    past = datetime.timedelta(days = days_from_current)
    return str(date.today() - past)


def get_past_stock_value(ticker, num_days):
    past_value = tuple(get_data(ticker, get_past_date(num_days), date.today())['close'].values.tolist())
    return past_value[0]


def datetime_list_convert(list_in):
    new_list = []
    for i in range(len(list_in)):
        new_list.append(str(list_in[i]))
    return new_list


def get_stock_value_list(ticker, num_days):
    close_stock_values = tuple(get_data(ticker, get_past_date(num_days), date.today())['close'].values.tolist())
    close_stock_dates = datetime_list_convert(tuple(get_data(ticker, get_past_date(num_days),
                                                             date.today()).index.tolist()))
    stock_value_list = {}
    for i in range(len(close_stock_values)):
        stock_value_list[close_stock_dates[i]] = round(close_stock_values[i], 2)

    return stock_value_list


def add_missing_dates(list_in):
    list_keys = list(list_in.keys())
    extra_list = {}
    for i in range(len(list_keys) - 1):
        if (date(int(list_keys[i + 1][0:4]), int(list_keys[i + 1][5:7]), int(list_keys[i + 1][8:10])) - date(int(list_keys[i][0:4]), int(list_keys[i][5:7]), int(list_keys[i][8:10]))).days > 1:
            diff = (date(int(list_keys[i + 1][0:4]), int(list_keys[i + 1][5:7]), int(list_keys[i + 1][8:10])) -
            date(int(list_keys[i][0:4]), int(list_keys[i][5:7]), int(list_keys[i][8:10]))).days
            for j in range(diff):
                extra_list[str(date(int(list_keys[i][0:4]), int(list_keys[i][5:7]), int(list_keys[i][8:10]))
                           + datetime.timedelta(days = j))] = list_in[list_keys[i]]

    return {**list_in, **extra_list}


#CALL THIS INSTEAD OF get_stock_value_list!!!
def get_fixed_stock_value_list(ticker, num_days):
    warnings.simplefilter('ignore')
    dict1 = add_missing_dates(get_stock_value_list(ticker, num_days))
    list1 = dict1.values()
    return list1


def ticker_to_name(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']
