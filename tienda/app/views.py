from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def home (request):
    return render (request, 'app/home.html')

def contacto (request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "contacto guardado"
        else:
            data['form'] = formulario


    return render (request, 'app/contacto.html', data)

def shop (request):
    return render (request, 'app/shop.html')

def somos (request):
    return render (request, 'app/somos.html')

def registro (request):
    return render (request, 'app/registro.html')