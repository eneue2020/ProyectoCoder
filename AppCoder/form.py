
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserEditForm(UserCreationForm):

    email=forms.EmailField(label="Modificar")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','password1','password2']
        help_text={k:"" for k in fields}

