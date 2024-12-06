from django.contrib import admin
from .models import Encuesta, Pregunta, Respuesta, RespuestaPregunta, Calificacion
# Register your models here.


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('titulo',)
    date_hierarchy = 'fecha_actualizacion'

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pregunta', 'encuesta', 'fecha_actualizacion')
    search_fields = ('texto_pregunta', 'respuesta')
    list_filter = ['encuesta']
    date_hierarchy = 'fecha_actualizacion'

class RespuestaPreguntaAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario', 'pregunta', 'respuesta')

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(RespuestaPregunta, RespuestaPreguntaAdmin)
admin.site.register(Calificacion)