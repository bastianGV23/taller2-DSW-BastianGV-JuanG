from django.shortcuts import render,redirect
from apps.formulario.forms import Formulario
from apps.formulario.models import Contacto
from django_tables2 import RequestConfig
from .tabla import tablaContacto
# Create your views here.

def index(request):
    return render(request, 'formulario/index.html')
    
def formulario_view(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('index')
    else:
        form = Formulario()
    
    return render(request, 'formulario/contacto.html',{'form':form})

def lista_Contacto(request):
    table = tablaContacto(Contacto.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'formulario/listado.html', {'contacto': table})