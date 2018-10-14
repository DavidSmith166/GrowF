from rest_framework import viewsets
from .models import Stock, StockPrice, Closing, Portfolio
from .serializers import StockSerializer, StockPriceSerializer, ClosingSerializer, PortfolioSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockPriceViewSet(viewsets.ModelViewSet):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer


class ClosingViewSet(viewsets.ModelViewSet):
    queryset = Closing.objects.all()
    serializer_class = ClosingSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer