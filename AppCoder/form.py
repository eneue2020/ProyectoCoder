
from django import forms

class Curso_Formulario(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre del Curso')
    camada = forms.IntegerField(label='Camada')


class Estudiante_Formulario(forms.Form):
    nombre=forms.CharField(max_length=40, label='Nombre del estudiante')
    apellido=forms.CharField(max_length=40, label='Apellido del estudiante')
    email=forms.EmailField(max_length=60,label='cuenta de mail')
    
   
class Profesor_Formulario(forms.Form):
    nombre=forms.CharField(max_length=40,label='Nombre del profesor')
    email=forms.EmailField(max_length=60,label='cuenta email profesor')
    profesion=forms.CharField(max_length=40,label='Profesion')

