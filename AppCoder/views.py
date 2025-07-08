from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.template import loader
from AppCoder.form import CursoForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect



# Create your views here.
def cursos(request):
    return HttpResponse("Lista de cursos")

def cursos(request):
    cursos = Curso.objects.all()  # Obtiene todos los cursos de la base de dato
    dicc= {'cursos': cursos}  # Crea un diccionario con los cursos
    plantilla = loader.get_template('AppCoder/cursos.html')  # Carga la plantilla HTML
    documento = plantilla.render(dicc)  # Renderiza la plantilla con el diccionario
    return HttpResponse(documento)  # Devuelve la respuesta HTTP con el contenido renderizado



def alta_curso(request, nombre):
    
    curso=Curso(nombre=nombre, camada=9999)
    curso.save()  # Guarda el curso en la base de datos
    msj= f"Curso {curso.nombre}, {curso.camada} dado de alta"
    
    return HttpResponse(msj)

def curso_formulario(request):
    if request.method == 'POST':
       mi_formulario=curso_formulario = CursoForm(request.POST)  # Crea una instancia del formulario con los datos enviados
       if mi_formulario.is_valid():  # Verifica si el formulario es válido
            datos = mi_formulario.cleaned_data  # Obtiene los datos limpios del formulario
            Curso = Curso(nombre=datos['nombre'], camada=datos['camada'])  # Crea un nuevo objeto Curso con los datos del formulario
            Curso.save()  # Guarda el curso en la base de datos
            return redirect('cursos')  # Redirige a la vista de cursos después de guardar el curso
    else:
        mi_formulario = CursoForm()
    return render(request, 'AppCoder/curso_formulario.html', {'formulario': mi_formulario})  # Renderiza el formulario para crear un curso


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes.html', {'estudiantes': estudiantes})

def profesores(request):
    profesores = Profesor.objects.all()  # Obtiene todos los profesores de la base de datos
    dicc = {'profesores': profesores}  # Crea un diccionario con los profesores
    plantilla = loader.get_template('AppCoder/profesores.html')  # Carga la plantilla HTML
    documento = plantilla.render(dicc)  # Renderiza la plantilla con el diccionario
    return HttpResponse(documento)  # Devuelve la respuesta HTTP con el contenido renderizado

def entregables(request):
    entregables = Entregable.objects.all()  # Obtiene todos los entregables de la base de datos
    dicc = {'entregables': entregables}  # Crea un diccionario con los entregables
    plantilla = loader.get_template('AppCoder/entregables.html')  # Carga la plantilla HTML
    documento = plantilla.render(dicc)  # Renderiza la plantilla con el diccionario
    return HttpResponse(documento)  # Devuelve la respuesta HTTP con el contenido renderizado

def contacto(request):
    return render(request, 'AppCoder/contacto.html')  # Renderiza la plantilla de contacto


