from django.urls import path
from . import views

urlpatterns = [
    path('', views.function_01, name='function_01')
]