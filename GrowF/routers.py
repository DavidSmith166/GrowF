from rest_framework import routers
from api.viewsets import StockViewSet, StockPriceViewSet, ClosingViewSet, PortfolioViewSet

router = routers.DefaultRouter()

router.register(r'stock', StockViewSet)
router.register(r'stockprice', StockPriceViewSet)
router.register(r'closing', ClosingViewSet)
router.register(r'portfolio', PortfolioViewSet)
