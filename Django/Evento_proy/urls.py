from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # Rutas para las páginas del sitio
    path('', views.index, name='index'),
    path('registrar_evento/', views.registrar_evento, name='registrar_evento'),
    path('eventos_agendados/', views.eventos_agendados, name='eventos_agendados'),
    path('evento_list/', views.evento_list, name='evento_list'),
    path('eliminar_evento/<int:id>/', views.eliminar_evento, name='eliminar_evento'),
    path('signin/', views.signin, name='signin'),
    path('editar_evento/', views.editar_evento, name='editar_evento'),

    # Rutas para el inicio de sesión
    path('login/', views.login_view, name='login'),
]

# Sirve archivos estáticos y multimedia en desarrollo
urlpatterns += static('media/', document_root='media')
