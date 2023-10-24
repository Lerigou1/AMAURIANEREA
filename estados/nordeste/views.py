from django.shortcuts import render

# Create your views here.
def nordeste(request):
    return render(request, 'nordeste.html')

def ceara(request):
    return render(request, 'ceara.html')

def bahia(request):
    return render(request, 'bahia.html')

def pernambuco(request):
    return render(request, 'pernambuco.html')

