from rest_framework import serializers
from .models import Stock, Portfolio, StockPrice, Closing


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = '__all__'


class ClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closing
        fields = '__all__'