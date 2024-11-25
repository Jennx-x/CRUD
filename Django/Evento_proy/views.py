from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Concierto, Conferencia
from django.http import HttpResponseBadRequest, JsonResponse
import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index(request):
    """
    Vista que muestra todos los eventos disponibles (conciertos, conferencias, eventos base).
    """
    eventos = Evento.objects.all()  # Obtiene todos los eventos base (incluyendo conciertos y conferencias)
    
    return render(request, 'index.html', {'eventos': eventos})

def registrar_evento(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('eventName')
        fecha_str = request.POST.get('eventDate')
        lugar = request.POST.get('eventPlace')

        if not (nombre and fecha_str and lugar):
            return HttpResponseBadRequest("Faltan campos obligatorios")

        try:
            fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponseBadRequest("Fecha no válida")

        # Aquí usamos solo get_or_create para evitar duplicados
        evento, created = Evento.objects.get_or_create(
            _nombre=nombre,
            _fecha=fecha,
            _lugar=lugar
        )

        # Si el evento ya existe, no lo creamos de nuevo
        if not created:
            return HttpResponseBadRequest("Este evento ya está registrado")

        # Registrar como concierto, si corresponde
        artista = request.POST.get('eventArtist')
        duracion = request.POST.get('eventDuration')
        if artista and duracion:
            Concierto.objects.create(
                _nombre=evento._nombre,
                _fecha=evento._fecha,
                _lugar=evento._lugar,
                _artista=artista,
                _duracion=duracion
            )

        # Registrar como conferencia, si corresponde
        tema = request.POST.get('eventTheme')
        orador = request.POST.get('eventSpeaker')
        if tema and orador:
            Conferencia.objects.create(
                _nombre=evento._nombre,
                _fecha=evento._fecha,
                _lugar=evento._lugar,
                _tema=tema,
                _orador=orador
            )
        
        return redirect('index')  # Redirigir a la página principal
    return HttpResponseBadRequest("Método no permitido")

def eventos_agendados(request):
    """
    Vista que muestra todos los eventos agendados.
    """
    eventos = Evento.objects.all()  # Puedes modificar esto según tus necesidades
    return render(request, 'eventos_agendados.html', {'eventos': eventos})

def evento_list(request):
    eventos = Evento.objects.all()  # Obtenemos todos los eventos
    return render(request, 'index.html', {'eventos': eventos})  # Renderizamos en index.html

def eliminar_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
        evento.delete()
        return redirect('index')  # Aquí redirigimos al index
    except Evento.DoesNotExist:
        return render(request, 'index.html', {'error': 'Evento no encontrado'})

# Vista para la página de inicio de sesión (signin)
def signin(request):
    return render(request, 'signin.html')

def editar_evento(request):
    if request.method == 'POST':
        # Recibir los datos enviados a través de AJAX
        evento_id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        artista = request.POST.get('artista')
        duracion = request.POST.get('duracion')
        tema = request.POST.get('tema')
        orador = request.POST.get('orador')

        # Buscar el evento y actualizar sus valores
        try:
            evento = Evento.objects.get(id=evento_id)
            evento.nombre = nombre
            evento.fecha = fecha
            evento.hora = hora
            evento.lugar = lugar
            evento.save()

            # Actualizar los campos específicos para conciertos y conferencias si existen
            if hasattr(evento, 'concierto'):
                if artista: 
                    evento.concierto.artista = artista
                if duracion: 
                    evento.concierto.duracion = duracion
                evento.concierto.save()

            if hasattr(evento, 'conferencia'):
                if tema: 
                    evento.conferencia.tema = tema
                if orador: 
                    evento.conferencia.orador = orador
                evento.conferencia.save()

            return JsonResponse({'success': True, 'message': 'Evento actualizado correctamente'})
        except Evento.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Evento no encontrado'})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

#SIGNIN

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir al índice después de iniciar sesión correctamente
        else:
            return render(request, 'signin.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'signin.html')