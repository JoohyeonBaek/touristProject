from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function_01(request):
    return render(request, 'function_01.html')
