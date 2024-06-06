from django import forms
from django.forms import ModelForm
from myapp.models import *

class RoupaForm(forms.ModelForm):
    class Meta:

        model = Roupa
        fields = "__all__"
        labels = {
            "title": "Título",
            "descript": "Descrição",
            "path": "Imagem",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            )
        }

