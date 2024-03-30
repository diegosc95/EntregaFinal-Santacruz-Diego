from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *

class Registrousuario(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class Editarusuario(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

class Editarusuario_name(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = ["username"]

class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField()


