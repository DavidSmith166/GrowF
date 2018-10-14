from django.contrib import admin
from .models import Stock, Closing, Portfolio, StockPrice
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'stock_prices']


@admin.register(Closing)
class ClosingAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ['stocks']

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    pass
