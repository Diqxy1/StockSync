from django.urls import path

from . import views

app_name = 'stock'

urlpatterns = [
    path('', views.ProductStockList.as_view(), name='list'),
    path('create/', views.ProductStockCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProductStockUpdate.as_view(), name='update'),
    path('sub/<int:pk>/', views.ProductStockSub.as_view(), name='sub'),
]
