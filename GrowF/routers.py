from rest_framework import routers
from api.viewsets import StockViewSet

router = routers.DefaultRouter()

router.register(r'stock', StockViewSet)