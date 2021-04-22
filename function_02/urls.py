from django.urls import path
from . import views

urlpatterns = [
    path('', views.function_02, name='function_02')
]