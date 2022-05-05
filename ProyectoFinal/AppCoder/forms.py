#from socket import fromshare
from django import forms
#importo para manejo de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#importo el modelo de albun de imagenes
#from .models import AlbumImage

class cursoformulario(forms.Form):
    cuit=forms.IntegerField()
    articulo=forms.CharField()
    cantidad=forms.IntegerField()

class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class UserEdithForm(UserCreationForm):
    email= forms.EmailField(label="Modificar Correo")
    password1=forms.CharField(label="ingrese la contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["email","password1","password2"]
        helptexts={k: "" for k in fields}



class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UploadImageForm(forms.ModelForm):

#     class Meta:
#         model = AlbumImage
#         fields = ['album', 'image']