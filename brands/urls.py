from django.urls import path

from . import views

app_name = 'brands'

urlpatterns = [
    path('', views.BrandList.as_view(), name='list'),
    path('create/', views.BrandCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.BrandUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BrandDelete.as_view(), name='delete'),
]
