from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from cuenta.models import TokensUser

# Create your views here.
def home(request):

    archivo_politicas = PoliticasDatos.objects.first()

    data = {
        'archivo_politicas': archivo_politicas,
    }

    return render(request, 'index.html', {'object_list': data})
#Vista para listar encuestas

class EncuestasListView(ListView):
    model = Encuesta
    template_name = 'encuesta/listar_encuestas.html'
    # context_object_name = 'encuestas'

    def get_queryset(self):
        archivo_politicas = PoliticasDatos.objects.first()
        return_object = {}
        return_object['archivo_politicas'] = archivo_politicas
        return_object['encuestas'] = self.model.objects.all()

        return return_object

        


class CrearEncuesta(CreateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'encuesta/crear_encuesta.html'
    success_url = reverse_lazy('listar_encuestas')

class EditarEncuesta(UpdateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = 'encuesta/editar_encuesta.html'
    success_url = reverse_lazy('listar_encuestas')

class EliminarEncuesta(DeleteView):
    model = Encuesta
    template_name = 'encuesta/eliminar_encuesta.html'
    success_url = reverse_lazy('listar_encuestas')

class DetalleEncuesta(DetailView):
    model = Encuesta
    template_name = 'encuesta/detalle_encuesta.html'
    context_object_name = 'encuesta'
#Vista para listar Preguntas

class PreguntaListView(ListView):
    model = Pregunta
    template_name = 'pregunta/listar_preguntas.html'
    context_object_name = 'preguntas'

class CrearPregunta(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'pregunta/crear_pregunta.html'
    success_url = reverse_lazy('listar_preguntas')

class EditarPregunta(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'pregunta/editar_pregunta.html'
    success_url = reverse_lazy('listar_preguntas')

class EliminarPregunta(DeleteView):
    model = Pregunta
    template_name = 'pregunta/eliminar_pregunta.html'
    success_url = reverse_lazy('listar_preguntas')

class DetallePregunta(DetailView):
    model = Pregunta
    template_name = 'pregunta/detalle_pregunta.html'
    context_object_name = 'pregunta'

def respuesta_usuario(request, id_encuesta):

    encuesta = Encuesta.objects.get(id=id_encuesta)
    preguntas = Pregunta.objects.filter(encuesta=encuesta)

    if request.method == 'POST':
        for pregunta in preguntas:
            respuesta_pregunta = request.POST.get(str(pregunta.id))
            
            if respuesta_pregunta:
                #verificar si el usuario ya respondio la pregunta
                if not RespuestaPregunta.objects.filter(pregunta=pregunta, usuario=request.user).exists():
                    respuesta_pregunta = RespuestaPregunta.objects.create(
                        usuario=request.user,
                        pregunta=pregunta,
                        respuesta=respuesta_pregunta
                    )
                else:
                    print(f'La pregunta {pregunta.texto_pregunta} ya ha sido respondida por el usuario {request.user.username}')

        guardar_respuesta = Respuesta.objects.create(
            encuesta=encuesta,
            usuario=request.user
        )  
        return redirect('lista_encuestas_respondidas')       

    data = {
        'encuesta': encuesta,
        'preguntas': preguntas,
    }

    return render(request, 'encuesta/respuesta_encuesta.html', data)

def lista_encuestas_respondidas(request):
    encuestas2 = Encuesta.objects.all()
    print(encuestas2)
    encuestas = Encuesta.objects.all().exclude(id__in=Respuesta.objects.filter(usuario=request.user).values_list('encuesta', flat=True))
    lista_encuestas_respondidas = Encuesta.objects.filter(id__in=Respuesta.objects.filter(usuario=request.user).values_list('encuesta', flat=True))

    
    calificaciones = Calificacion.objects.filter(encuesta__in=lista_encuestas_respondidas).values_list('encuesta_id', flat=True)

    return render(request, 'encuesta/lista_encuestas_respondidas.html', {'encuestas': encuestas, 'lista_encuestas_respondidas': lista_encuestas_respondidas, 'calificaciones': calificaciones})

def ver_respuestas(request, id_encuesta):

    preguntas = Pregunta.objects.filter(encuesta_id=id_encuesta)
    calificar_encuestas = None
    if Calificacion.objects.filter(encuesta_id=id_encuesta, usuario_id=request.user.id).exists():
        calificar_encuestas = Calificacion.objects.get(encuesta_id=id_encuesta, usuario_id=request.user.id)

    
    return render(request, 'encuesta/ver_respuestas.html', {'preguntas': preguntas, 'calificar_encuestas': calificar_encuestas})

def calificar_encuestas(request, id_encuesta):
    encuesta = Encuesta.objects.get(id=id_encuesta)
    if request.method == 'POST':
        form = FormularioCalificacion(request.POST)
        if form.is_valid():
            form.instance.encuesta_id = id_encuesta
            form.instance.usuario_id = request.user.id
            form.save()  
            return redirect('lista_encuestas_respondidas')
    else:
        form = FormularioCalificacion()


    return render(request, 'encuesta/calificar_encuestas.html', {'form': form, 'encuesta': encuesta})


from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status
## Vistas DRF API

## APIView Necesitamos crear una vista por metodo del API

#Vista GET, POST

#secci+on de encuestas
class EncuestaViewCreate(APIView):
    def get(self, request):
        encuestas = Encuesta.objects.all()
        serializer = EncuestaSerializer(encuestas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EncuestasDetalle(APIView):
    def get(self, request, pk):
        encuesta = Encuesta.objects.get(id=pk)
        if encuesta is not None:
            serializer = EncuestaSerializer(encuesta)
            return Response(serializer.data)
        return Response({'detail': 'Encuesta no encontrada'},status=status.HTTP_404_NOT_FOUND)

    def put(self,request, pk):
        print('ENTRA A PUT', pk)
        encuesta = Encuesta.objects.get(id=2)
        if encuesta is not None:
            serializer = EncuestaSerializer(encuesta, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Encuesta no encontrada'},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        encuesta = Encuesta.objects.get(id=pk)
        encuesta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#secci+on de preguntas
class PreguntaViewCreate(APIView):
    def get(self, request):
        preguntas = Pregunta.objects.all()
        serializer = PreguntaSerializer(preguntas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PreguntaDetalle(APIView):
    def get(self, request, pk):
        pregunta = Pregunta.objects.get(id=pk)
        if pregunta is not None:
            serializer = PreguntaSerializer(pregunta)
            return Response(serializer.data)
        return Response({'detail': 'pregunta no encontrada'},status=status.HTTP_404_NOT_FOUND)

    def put(self,request, pk):
        print('ENTRA A PUT', pk)
        pregunta = Pregunta.objects.get(id=2)
        if pregunta is not None:
            serializer = PreguntaSerializer(pregunta, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'pregunta no encontrada'},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        pregunta = Pregunta.objects.get(id=pk)
        if pregunta is not None:
            pregunta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'pregunta no encontrada'},status=status.HTTP_404_NOT_FOUND)




# viewsets.ModelViewSet este contiene todo el CRUD solo cambia el metodo que se envia por el api POST, GET, PUT y DELETE
class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


from django.http import JsonResponse
from decouple import config
from django.core.cache import cache

def actualizar_encuesta_ajax(request,encuesta_id):
    

    # encuesta = Encuesta.objects.get(id=encuesta_id)
    encuesta = get_object_or_404(Encuesta, id=encuesta_id)

    encuestas_cache = cache.get('encuesta')
    print('encuestas_cache', encuestas_cache)
    if encuestas_cache is None:
        cache.set('encuesta', encuesta)

    varible_env = config('VARIABLE_1')
    print(varible_env)

    if request.method == 'POST':
        form = EncuestaForm(request.POST, instance=encuesta)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Encuesta actualizada correctamente',
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Error al actualizar la encuesta',
            })
    else:
        form = EncuestaForm(instance=encuesta)
    
    return render(request, 'encuesta/actualizar_encuesta.html', {'form': form, 'encuesta': encuesta})


from django.db.models import Avg, Count

def ejemplo_select_relate(request):
    # preguntas = Pregunta.objects.select_related('encuesta').all()
    # preguntas_sinselect = Pregunta.objects.all()
    # # print('preguntas', preguntas)
    # print('preguntas_sinselect', preguntas_sinselect)


    # preguntas = Pregunta.objects.values_list('id', 'texto_pregunta')

    # for pregunta in preguntas:
    #     print(pregunta)

    tamanno = Encuesta.objects.aggregate(Avg('descripcion'))

    print('tamanno', tamanno)


def cargar_documento(request):
    if request.method == 'POST':
        form = PoliticasDatosForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('listar_encuestas')
    else:
        form = PoliticasDatosForm()
    
    return render(request, 'encuesta/cargar_documento.html', {'form': form})


from .tasks import suma
def ejecuta_tarea(request):
    
    resultado = suma.delay(2,8)
    return render(request, 'encuesta/cargar_documento.html', {'resultado': resultado})


from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def crear_encuesta_api(request):
    if request.method == 'POST':
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def actualizar_encuesta_api(request, pk):
    try:
        encuesta = Encuesta.objects.get(pk=pk)
    except Encuesta.DoesNotExist:
        return Response({'error': 'Encuesta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EncuestaSerializer(encuesta, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detalle_encuesta_api(request, pk):
    try:
        encuesta = Encuesta.objects.get(pk=pk)
    except Encuesta.DoesNotExist:
        return Response({'error': 'Encuesta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EncuestaSerializer(encuesta)
    return Response(serializer.data)


def consultas_select(request):

    preguntas = Pregunta.objects.select_related('encuesta').all()

    for pregunta in preguntas:
        print(pregunta.encuesta.titulo)


@api_view(['DELETE'])
def eliminar_encuesta_api(request, pk):
    try:
        encuesta = Encuesta.objects.get(pk=pk)
    except Encuesta.DoesNotExist:
        return Response({'error': 'Encuesta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    encuesta.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#Validar usuario logueado y retornar su id
from rest_framework_simplejwt.tokens import AccessToken
@api_view(['GET'])
def get_user_id(request):
    print('entrar')

    token = request.headers.get('Authorization')
    print('token', token)

    try:
        usuario_id = TokensUser.objects.get(token=token)
        print('usuario_id', usuario_id.id)

        # return Response({'usuario_id': usuario_id.id})
        return Response({'usuario_id': usuario_id.id}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)


# Sección de Respuestas

class RespuestasViewCreate(APIView):
    def get(self, request, user_id):
        encuestas = Respuesta.objects.filter(usuario_id=user_id)
        serializer = RespuestaSerializer(encuestas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = RespuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    