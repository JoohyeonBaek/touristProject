from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_03, name='analysis_03')
]