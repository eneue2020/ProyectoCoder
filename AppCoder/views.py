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
       mi_formulario=CursoForm(request.POST)  # Crea una instancia del formulario con los datos enviados
       if mi_formulario.is_valid():  # Verifica si el formulario es válido
            datos = mi_formulario.cleaned_data  # Obtiene los datos limpios del formulario
            Curso = Curso(nombre=datos['nombre'], camada=datos['camada'])  # Crea un nuevo objeto Curso con los datos del formulario
            Curso.save()  # Guarda el curso en la base de datos
            return render( request , "padre.html")  

    return render(request, 'AppCoder/formulario.html')  # Renderiza el formulario para crear un curso


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


def buscar_curso(request):
    return render(request , "buscar_curso.html")


def buscar(request):
    
    if request.POST["nombre"]:
        cursos = Curso.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("No se ha encontrado nada")


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request, "AppCoder/cursos.html" , {"cursos":curso})


def editar( request , id ):
    curso = Curso.objects.get(id=id) 
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()
            return render(request , "AppCoder/cursos.html" , {"cursos":curso})
    else:
        mi_formulario = CursoForm(initial={'nombre':curso.nombre, 'camada':curso.camada})
    return render(request , "AppCoder/editar_curso.html" , {"mi_formulario":mi_formulario, "curso":curso })


