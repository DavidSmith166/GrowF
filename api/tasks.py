from concurrent.futures import ThreadPoolExecutor, as_completed
from .models import Stock, StockPrice
from .yahoo import get_current_stock_value
from background_task import background
from django.conf import settings


MAX_WORKER = 4


def chunk(my_list, number_of_chunks):
    chunk_size = int(len(my_list) / number_of_chunks)
    for i in range(0, number_of_chunks-1):
        yield my_list[i*chunk_size:i*chunk_size+chunk_size]
    yield my_list[number_of_chunks*chunk_size-chunk_size:]


@background()
def update_real_time_data():
    try:
        stocks = [stock.ticker for stock in Stock.objects.all()]
        with ThreadPoolExecutor(MAX_WORKER) as p:
            stock_updates = p.map(get_current_stock_value, stocks)
        for ticker, timestamp, value in stock_updates:
            StockPrice.objects.create(stock=Stock.objects.get(ticker=ticker), timestamp=timestamp, value=value)
    except Exception as e:
        print('Exception in background tasks of type {} : {}'.format(type(e), str(e)))


update_real_time_data(repeat=5, repeat_until=None)
