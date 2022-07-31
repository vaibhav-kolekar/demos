from django.shortcuts import render

# Create your views here.
def p2index(request):
    return render(request, 'p2/p2index.html')