from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def p2(request):
    return HttpResponse("P2!!!")

def inedx(request):
    return render(request, 'p2/index.html')