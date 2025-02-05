from rest_framework import serializers
from .models import Encuesta, Pregunta, Respuesta, Calificacion, RespuestaPregunta


class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class RespuestaPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPregunta
        fields = '__all__'