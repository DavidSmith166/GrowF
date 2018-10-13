from concurrent.futures import ThreadPoolExecutor, as_completed
from .models import Stock, StockPrice
from .yahoo import get_current_stock_value
from background_task import background
import numpy as np
from django.conf import settings


MAX_WORKER = 4


@background()
def update_real_time_data():
    try:
        stocks = [stock.ticker for stock in Stock.objects.all()]
        if len(stocks) >= MAX_WORKER:
            chunks = np.split(np.asarray(stocks), MAX_WORKER)
        else:
            chunks = stocks
        with ThreadPoolExecutor(MAX_WORKER) as p:
            stock_updates = p.map(get_current_stock_value, chunks)
        for ticker, timestamp, value in stock_updates:
            StockPrice.objects.create(stock=Stock.objects.get(ticker=ticker), timestamp=timestamp, value=value)
    except Exception as e:
        print(e)


update_real_time_data(repeat=5, repeat_until=None)
