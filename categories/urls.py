from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='list'),
    path('create/', views.CategoryCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.CategoryUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.CategoryDelete.as_view(), name='delete'),
]
