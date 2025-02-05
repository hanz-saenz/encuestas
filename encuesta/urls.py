from django.contrib import admin
from django.urls import path, include
# from .views import home, EncuestasListView, CrearEncuesta, EditarEncuesta, EliminarEncuesta, DetalleEncuesta, PreguntaListView, CrearPregunta
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('encuestas-view', EncuestaViewSet)
router.register('preguntas-view', PreguntaViewSet)


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



    ### url DRF API
    #encuestas
    path('api/encuestas/', EncuestaViewCreate.as_view(), name='encuesta-list-create'),
    path('api/encuestas/<int:pk>/', EncuestasDetalle.as_view(), name='encuesta-list-detalle'),
    #preguntas
    
    path('api/preguntas/', PreguntaViewCreate.as_view(), name='preguntas-list-create'),
    path('api/preguntas/<int:pk>/', PreguntaDetalle.as_view(), name='preguntas-list-detalle'),
    path('api/', include(router.urls)),

    #AJAX
    path('actualizar/<int:encuesta_id>/', actualizar_encuesta_ajax, name='encuesta-actuyalizar'),
    path('select_relate/', ejemplo_select_relate),
    path('api/crear/encuesta', crear_encuesta_api, name='crear_encuesta_api'),
    path('api/editar/encuesta/<int:pk>', actualizar_encuesta_api, name='actualizar_encuesta_api'),
    path('api/consultar/encuesta/<int:pk>', detalle_encuesta_api, name='detalle_encuesta_api'),
    path('api/eliminar/encuesta/<int:pk>', eliminar_encuesta_api, name='eliminar_encuesta_api'),


    #
    #validar usuario con token
    path('api/obtener/usuario/', get_user_id, name='get_user_id'),
    # API de respuestas

    path('api/respuestas/<int:user_id>', RespuestasViewCreate.as_view(), name='respiestas-list-create'),
    #ejemplo select_relate
    path('select/', consultas_select, name='consultas_select'),
    # path('api/encuestas-view/', EncuestaView.as_view(), name='encuesta-list-'),
]
