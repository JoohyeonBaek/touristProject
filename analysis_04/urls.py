from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_04, name='analysis_04')
]