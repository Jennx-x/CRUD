from django.db import models

# Modelo es una clase (MTV) que, a través de un ORM (Object Relational Mapping), nos permite interactuar con POO.

# Clase base: Evento
class Evento(models.Model):
    # Atributos encapsulados
    _nombre = models.CharField(max_length=200)  # Nombre del evento
    _fecha = models.DateField()  # Fecha del evento
    _lugar = models.CharField(max_length=200)  # Lugar del evento

    # Propiedades para acceder a los atributos encapsulados
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def lugar(self):
        return self._lugar

    @lugar.setter
    def lugar(self, value):
        self._lugar = value

    # Método para representar el evento de forma legible
    def __str__(self):
        return f"{self.nombre} - {self.fecha} en {self.lugar}"

    # Método estático para calcular el costo total de las boletas
    @staticmethod
    def calcular_costo_boletas(cantidad_boletas, precio_por_boleta):
        """
        Calcula el costo total basado en la cantidad y el precio de cada boleta.
        """
        if cantidad_boletas > 0 and precio_por_boleta > 0:
            return cantidad_boletas * precio_por_boleta
        return None

    # Método de clase para crear un evento desde un diccionario
    @classmethod
    def crear_desde_diccionario(cls, data):
        """
        Crea un evento usando un diccionario con los datos necesarios.
        """
        return cls.objects.create(
            _nombre=data['nombre'],
            _fecha=data['fecha'],
            _lugar=data['lugar']
        )

# Clase hija: Concierto (hereda de Evento)
class Concierto(Evento):
    # Atributos encapsulados adicionales
    _artista = models.CharField(max_length=200)  # Nombre del artista
    _duracion = models.CharField(max_length=50)  # Duración del concierto

    # Propiedades para acceder a los atributos encapsulados
    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, value):
        self._artista = value

    @property
    def duracion(self):
        return self._duracion   

    @duracion.setter
    def duracion(self, value):
        self._duracion = value

    # Método para representar el concierto de forma legible
    def __str__(self):
        return f"{self.nombre} - {self.artista} en {self.lugar}"

    # Método de clase para crear un concierto desde un diccionario
    @classmethod
    def crear_desde_diccionario(cls, data):
        """
        Crea un concierto usando un diccionario con los datos necesarios.
        """
        return cls.objects.create(
            _nombre=data['nombre'],
            _fecha=data['fecha'],
            _lugar=data['lugar'],
            _artista=data['artista'],
            _duracion=data['duracion']
        )

# Clase hija: Conferencia (hereda de Evento)
class Conferencia(Evento):
    # Atributos encapsulados adicionales
    _tema = models.CharField(max_length=200)  # Tema de la conferencia
    _orador = models.CharField(max_length=200)  # Orador de la conferencia

    # Propiedades para acceder a los atributos encapsulados
    @property
    def tema(self):
        return self._tema

    @tema.setter
    def tema(self, value):
        self._tema = value

    @property
    def orador(self):
        return self._orador

    @orador.setter
    def orador(self, value):
        self._orador = value

    # Método para representar la conferencia de forma legible
    def __str__(self):
        return f"{self.nombre} - {self.tema} en {self.lugar}"

    # Método de clase para crear una conferencia desde un diccionario
    @classmethod
    def crear_desde_diccionario(cls, data):
        """
        Crea una conferencia usando un diccionario con los datos necesarios.
        """
        return cls.objects.create(
            _nombre=data['nombre'],
            _fecha=data['fecha'],
            _lugar=data['lugar'],
            _tema=data['tema'],
            _orador=data['orador']
        )

