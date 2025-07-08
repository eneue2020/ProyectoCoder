
from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre del Curso')
    camada = forms.IntegerField(label='Camada')
   