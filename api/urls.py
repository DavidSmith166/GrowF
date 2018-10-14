from django.conf.urls import url
from .views import StockListApiView, StockRetrieveApiView

app_name = 'stock'

urlpatterns = [
    url(r'^stocks/$', StockListApiView.as_view()),
    url(r'^stocks/(?P<cat_id>\w+)/?$', StockRetrieveApiView.as_view()),
]
