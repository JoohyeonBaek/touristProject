from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_02(request):
    return render(request, 'analysis_02.html')
