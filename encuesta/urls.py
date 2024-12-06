from django.contrib import admin
from django.urls import path
# from .views import home, EncuestasListView, CrearEncuesta, EditarEncuesta, EliminarEncuesta, DetalleEncuesta, PreguntaListView, CrearPregunta
from .views import *


urlpatterns = [
    # path('', home, name='index'),
    path('', EncuestasListView.as_view(), name='listar_encuestas'),
    path('crear/', CrearEncuesta.as_view(), name='crear_encuesta'),
    path('editar/<int:pk>', EditarEncuesta.as_view(), name='editar_encuesta'),
    path('eliminar/<int:pk>', EliminarEncuesta.as_view(), name='eliminar_encuesta'),
    path('detalle/<int:pk>', DetalleEncuesta.as_view(), name='detalle_encuesta'),

    ## urls preguntas
    path('preguntas/', PreguntaListView.as_view(), name='listar_preguntas'),
    path('crear/pregunta/', CrearPregunta.as_view(), name='crear_pregunta'),
    path('editar/pregunta/<int:pk>', EditarPregunta.as_view(), name='editar_pregunta'),
    path('eliminar/pregunta/<int:pk>', EliminarPregunta.as_view(), name='eliminar_pregunta'),
    path('detalle/pregunta/<int:pk>', DetallePregunta.as_view(), name='detalle_pregunta'),
    path('respuesta/<int:id_encuesta>', respuesta_usuario, name='respuesta_usuario'),
    path('respuestas/', lista_encuestas_respondidas, name='lista_encuestas_respondidas'),
    path('ver_respuestas/<int:id_encuesta>', ver_respuestas, name='ver_respuestas'),
    path('calificacion/<int:id_encuesta>', calificar_encuestas, name='calificar_encuesta'),
]
