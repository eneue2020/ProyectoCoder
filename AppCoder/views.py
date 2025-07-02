from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.template import loader


# Create your views here.
def cursos(request):
    return HttpResponse("Lista de cursos")

def cursos(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos de la base de dato
    dicc= {'cursos': cursos}  # Crea un diccionario con los cursos
    plantilla = loader.get_template('cursos.html')  # Carga la plantilla HTML
    documento = plantilla.render(dicc)  # Renderiza la plantilla con el diccionario
    return HttpResponse(documento)  # Devuelve la respuesta HTTP con el contenido renderizado



def alta_curso(request, nombre):
    
    curso=Curso(nombre=nombre, camada=9999)
    curso.save()  # Guarda el curso en la base de datos
    msj= f"Curso {curso.nombre}, {curso.camada} dado de alta"
    
    return HttpResponse(msj)