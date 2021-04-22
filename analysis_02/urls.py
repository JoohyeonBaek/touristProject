from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_02, name='analysis_02')
]