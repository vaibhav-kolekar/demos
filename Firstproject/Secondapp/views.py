from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def funsecond(request):
    return HttpResponse("Hello wolrd from secondApp !!!")