from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.urls import reverse_lazy
from .forms import EncuestaForm, PreguntaForm, FormularioRespuestaPregunta, FormularioCalificacion

# Create your views here.
def home(request):
    return render(request, 'index.html')
#Vista para listar encuestas

class EncuestasListView(ListView):
    model = Encuesta
    template_name = 'encuesta/listar_encuestas.html'
    context_object_name = 'encuestas'

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
