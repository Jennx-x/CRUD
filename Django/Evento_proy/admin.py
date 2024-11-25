from django.contrib import admin

# Gestionar curso para hacer operaciones con el
# Register your models here.
from .models import Evento, Concierto, Conferencia #Importar modelo

admin.site.register(Evento)
admin.site.register(Concierto)
admin.site.register(Conferencia)
