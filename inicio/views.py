from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Ropa
from .forms import CrearIndumentariaFormulario, BuscarIndumentariaFormulario



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
    


def crear_indumentaria(request,prenda,marca,talla):
    ropa = Ropa(prenda=prenda,marca=marca,talla=talla)
    ropa.save()
    return render(request,'crear_indumentaria.html',{'ropa':ropa})

def buscar_indumentaria(request):
    
    formulario = BuscarIndumentariaFormulario(request.GET)
    if formulario.is_valid():
        prenda = formulario.cleaned_data.get('prenda')
        ropas = Ropa.objects.filter(prenda__icontains=prenda)
    else:
        ropas = Ropa.objects.all()
    
    return render(request,'inicio/buscar_indumentaria.html',{'ropas': ropas, 'form':formulario })

def crear_indumentarias(request):
    
    # print('Request', request)
    # print('GET', request.GET)
    # print('POST', request.POST)
    
    formulario = CrearIndumentariaFormulario()
    
    if request.method == 'POST':
        # ropa = Ropa(prenda=request.POST.get("prenda"),marca=request.POST.get('marca'),talla=request.POST.get('talla'))
        # ropa.save()
        
        
        formulario = CrearIndumentariaFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            ropa = Ropa(prenda=data.get("prenda"),marca=data.get('marca'),talla=data.get('talla'))
            ropa.save()                
            return redirect('inicio:buscar_indumentaria')
    
    return render(request,'inicio/crear_indumentarias.html',{'form':formulario})
     