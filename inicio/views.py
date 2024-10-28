from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from .models import Ropa
from .forms import Ropaformu

def inicio (request):
    # return HttpResponse('<h1>Inicio<h1/>')
    return render(request, 'index.html')

def datos(request, nombre):   
    nombres = nombre.upper()   
    return HttpResponse(f'kapo {nombres}')

def template1(request):

    with open(r'templates\template1.html') as abrir_template:
        template = Template(abrir_template.read())
    
    
    contexto = Context()
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)

def template2(request):
    fecha_actual = datetime.now()
    datos = {
        'fecha_actual': fecha_actual,
        'numeros': list(range(1,11))
        }
    
    #v1
    # with open(r'templates\template2.html') as abrir_template:
    #     template = Template(abrir_template.read())   
    # contexto = Context(datos)
    # render_template = template.render(contexto)
    
    #v2
    # template = loader.get_template('template2.html')
    # render_template = template.render(datos)
    # return HttpResponse(render_template)
    
    # V3
    
    return render(request,'template2.html',datos)
    
def Crear_Ropa(request):
    # ropa = Ropa(prenda=prenda, marca=marca, talla=talla)
    # ropa.save()
    # return render(request, 'Crear_Ropa.html', {'ropa' : ropa})
    form = Ropaformu(request.POST)
    form.save()
    return render(request, 'Crear_Ropa.html', {'ropa' : form})
    
    