from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable

admin.site.register(Curso)
admin.site.register(Estudiante) 
admin.site.register(Profesor)
admin.site.register(Entregable)
# Register your models here.
