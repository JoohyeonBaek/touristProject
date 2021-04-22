from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function_02(request):
    return render(request, 'function_02.html')
