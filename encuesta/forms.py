from django import forms
from .models import Encuesta, Pregunta, Respuesta, RespuestaPregunta, Calificacion, PoliticasDatos


class EncuestaForm(forms.ModelForm):
    
    class Meta:
        model = Encuesta
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ['encuesta','texto_pregunta', 'respuesta']
        widgets = {
            'encuesta': forms.Select(
                attrs={
                    'class': 'form-control'
            }),
            'texto_pregunta': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'respuesta': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }


class FormularioRespuesta(forms.ModelForm):

    class Meta:
        model = Respuesta
        fields = ['encuesta', 'usuario']
        widgets = {
            'encuesta': forms.Select(
                attrs={
                    'class': 'form-control'
            }),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control'
            }),
        }

class FormularioRespuestaPregunta(forms.ModelForm):

    class Meta:
        model = RespuestaPregunta
        fields = ['pregunta', 'respuesta']
        widgets = {
            'pregunta': forms.Select(
                attrs={
                    'class': 'form-control'
            }),
            'respuesta': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),
        }

class FormularioCalificacion(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = [ 'calificacion']
        widgets = {
            'calificacion': forms.Select(
                attrs={
                    'class': 'form-control'
            }),
        }

class PoliticasDatosForm(forms.ModelForm):

    class Meta:
        model = PoliticasDatos
        fields = ['archivo','titulo']