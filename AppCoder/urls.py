
from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos,name='cursos'),
    path('alta_curso/<nombre>/', views.alta_curso),
    #path('estudiantes/', views.estudiantes),
   # path('profesores/', views.profesor),
    #path('entregables/', views.entregables),
    #path('inicio/', views.inicio),
]
   
    