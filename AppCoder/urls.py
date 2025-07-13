
from django.urls import path
from . import views


urlpatterns = [
    path('cursos/', views.cursos, name='cursos'),
   # path('alta_curso/<nombre>/', views.alta_curso, name='alta_curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('entregables/', views.entregables, name='entregables'),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path("alta_curso/",views.curso_formulario,name="alta_curso"),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),    
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("alta_estudiante/",views.estudiante_formulario,name="alta_estudiante"),
    path("alta_profesor/",views.profesor_formulario,name='alta_profesor')
]
   
    