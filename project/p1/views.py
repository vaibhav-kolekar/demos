from django.shortcuts import render

# Create your views here.
def p1index(request):
    return render(request, 'p1/p1index.html')