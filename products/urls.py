from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('create/', views.ProductCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProductUpdate.as_view(), name='update'),
]
