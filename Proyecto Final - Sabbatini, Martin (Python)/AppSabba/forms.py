from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class PilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=20)
    marca_vehiculo = forms.CharField(max_length=40)
    modelo_vehiculo = forms.CharField(max_length=40)

class CopilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=20)





class RegistroFormulario(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingrese una contraseña:", widget=forms.PasswordInput) #ocultar
    password2 = forms.CharField(label="Repita su contraseña:",widget=forms.PasswordInput)

    class Meta:

        model = User #importamos modelo
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]