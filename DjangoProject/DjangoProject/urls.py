from django.contrib import admin
from django.urls import path
from DjangoService.views import BuyItemView, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:pk>/', BuyItemView.as_view(), name='buy-item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail')
]
