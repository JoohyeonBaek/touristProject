from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_04(request):
    return render(request, 'analysis_04.html')
