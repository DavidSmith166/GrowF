from rest_framework import routers
from web.viewsets import StockViewSet

router = routers.DefaultRouter()

router.register(r'stock', StockViewSet)