from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_03(request):
    return render(request, 'analysis_03.html')
