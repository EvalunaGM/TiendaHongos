from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'app/home.html')

def contacto (request):
    return render (request, 'app/contacto.html')

def shop (request):
    return render (request, 'app/shop.html')

def somos (request):
    return render (request, 'app/somos.html')

def registro (request):
    return render (request, 'app/registro.html')