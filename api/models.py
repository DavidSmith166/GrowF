from django.db import models
from django.core.exceptions import ValidationError
from .yahoo import get_current_stock_value, ticker_to_name


def validate_portfolio_name(value):
    if not len(value) <= 70:
        raise ValidationError('Portfolio name too long, must be less than 70 characters')

def validate_ticker(value):
    try:
        get_current_stock_value(value)
    except ValueError as e:
        raise ValidationError('Ticker does not exist')


class Portfolio(models.Model):
    name = models.CharField(max_length=70, unique=True, validators=[validate_portfolio_name])

    def __str__(self):
        return self.name

    @property
    def stocks(self):
        return list(Stock.objects.all().filter(portfolios=self)[:10])


class Stock(models.Model):
    ticker = models.CharField(max_length=4, unique=True, validators=[validate_ticker])
    portfolios = models.ManyToManyField(Portfolio, blank=True)

    def __str__(self):
        return self.ticker + ' : ' + self.name

    @property
    def name(self):
        return ticker_to_name(self.ticker.upper())

    @property
    def stock_prices(self):
        return list(StockPrice.objects.all().filter(stock=self)[:10])


class Closing(models.Model):
    date = models.DateField()
    percentile = models.DecimalField(max_digits=7, decimal_places=7)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, to_field='ticker')

    def __str__(self):
        return '{} : {} : {}'.format(self.stock, self.date, self.percentile)


class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, to_field='ticker')
    timestamp = models.DateTimeField()
    value = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return '{} : {} : {}'.format(str(self.stock), self.timestamp, self.value)


