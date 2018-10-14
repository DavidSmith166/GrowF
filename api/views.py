from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Stock
from .renderers import StockJSONRenderer
from .serializers import StockSerializer, StockListSerializer

class StockListApiView(ListAPIView):
    model = Stock
    queryset = Stock.objects.all()
    permissions_classes = (AllowAny, )
    renderer_classes = (StockJSONRenderer, )
    serializer_class = StockListSerializer

class StockRetrieveApiView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (StockJSONRenderer, )
    serializer_class = StockSerializer
    def retrieve(self, request, Stock, *args, **kwargs):
        stock = Stock.objects.get(id = stock.id) 
        serializer = self.serializer_class(stock)
        return Response(serializer.data, status = status.HTTP_200_OK)
