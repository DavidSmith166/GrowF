from yahoo_fin import stock_info
import warnings
from datetime import datetime

def get_current_stock_value(ticker):
    warnings.simplefilter('ignore')
    stock_value = round(stock_info.get_live_price(ticker), 2)
    return (ticker, datetime.now(), stock_value)