from django.db import models
from django.core.exceptions import ValidationError


def validate_portfolio_name(value):
    if not len(value) <= 70:
        raise ValidationError('Portfolio name too long, must be less than 70 characters')


class Portfolio(models.Model):
    name = models.CharField(max_length=70, validators=[validate_portfolio_name])


class Stock(models.Model):
    ticker = models.CharField(max_length=4, unique=True)
    portfolios = models.ManyToManyField(Portfolio, blank=True)

    def __str__(self):
        return self.ticker


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


