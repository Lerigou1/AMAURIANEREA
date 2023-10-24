from django.shortcuts import render

# Create your views here.
def norte(request):
    return render(request, 'norte.html')

def tocantins(request):
    return render(request, 'tocantins.html')

def acre(request):
    return render(request, 'acre.html')


