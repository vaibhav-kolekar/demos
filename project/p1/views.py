from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def p1(request):
    return HttpResponse("P1!!!")

def index(request):
    return render(request, 'p1/index.html')