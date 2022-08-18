import imp
from django.db import models
from django.http import HttpRequest
# Create your models here.

def p1(request):
    return HttpRequest("P1!!!")