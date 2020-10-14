from django.urls import path

from . import views

app_name = 'moviments'

urlpatterns = [
    path('exit/', views.StockExitMovement.as_view(), name='exit'),
    path('entry/', views.StockEntryMoviment.as_view(), name='entry'),
]
