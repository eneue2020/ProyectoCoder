
from django.urls import path
from . import views


urlpatterns = [
    path('cursos/', views.cursos, name='cursos'),
    path('alta_curso/<nombre>/', views.alta_curso, name='alta_curso'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores, name='profesores'),
    path('entregables/', views.entregables, name='entregables'),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto')
]
   
    