from django.contrib import admin
from .models import Stock, Closing, Portfolio, StockPrice
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Closing)
class ClosingAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    pass
