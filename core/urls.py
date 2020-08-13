from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_or_login, name='home_or_login'),
]
