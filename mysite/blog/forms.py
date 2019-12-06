from django import forms
from .models import Post
from .models import Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'nombre', 
            'correo',
            'contraseña',
        ]
        label = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'contraseña': 'Contraseña',
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)