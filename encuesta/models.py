from django.db import models
from django.contrib.auth.models import User

url_static = 'static/assets/imagenes'
# Create your models here.
class Encuesta(models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=100)
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"


class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    texto_pregunta = models.TextField(verbose_name="Pregunta")
    respuesta = models.TextField(verbose_name="Respuesta")
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return self.texto_pregunta

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

class Respuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return f"{self.encuesta.titulo} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


class RespuestaPregunta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.TextField(verbose_name="Respuesta")
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return f"{self.pregunta.texto_pregunta} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Respuesta a Preguntas"
        verbose_name_plural = "Respuestas a Preguntas"

class Calificacion(models.Model):

    CALIFICACIONES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    calificacion = models.IntegerField(verbose_name="Calificacion", choices=CALIFICACIONES)
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateField(verbose_name="Fecha de actualización", auto_now=True)

    def __str__(self):
        return f"{self.encuesta.titulo} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"


class PoliticasDatos(models.Model):
    titulo = models.CharField(verbose_name="Título",max_length=100)
    archivo = models.FileField(upload_to=f'{url_static}/politicas/', verbose_name="Archivo")
    fecha_creacion = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Política de Datos"
        verbose_name_plural = "Políticas de Datos"