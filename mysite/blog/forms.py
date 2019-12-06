from django import forms

from blog.models import Post

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
