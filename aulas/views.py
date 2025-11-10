from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello (request):  
    return HttpResponse("Hola compañeros")
def bye (request):  
    return HttpResponse("Adiós compañeros")
def edad (request, edad ,futuro):  
  incremento = futuro - date.today().year
  mensaje = "en el año " + str(futuro) + " tendrás " + str(edad + incremento) + " años"
  return HttpResponse(mensaje)
def segunda_plantilla (request):  
    tpl = get_template('segunda_plantilla.html')
      
    mensaje = tpl.render({
    'nombre':'Juan',
    'apellido':'Pérez'
    ,'fecha_actual':date.today()
    }
          
    )
    return HttpResponse(mensaje)
def tercer_plantilla (request):  
    return render(request,'tercer_plantilla.html',{
    'nombre':'Ana',
    'apellido':'García',
    'fecha_actual':date.today()
    })
class Empleado(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
       
def cuarta_plantilla (request):  
    empleado = Empleado('Luis','Martínez')
    laborales = ['Lunes','Martes','Miércoles','Jueves','Viernes']
    return render(request,'cuarta_plantilla.html',{
     'mi_empleado':empleado,
     'laborales':laborales,
    'fecha_actual':date.today()
    })