from django import template
from visualizador.models import *

register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def artista_album(id):
    return Album.objects.filter(artista=id)

@register.filter
def album_cancion(id):
    return Cancion.objects.filter(album=id)

@register.filter
def tablatura_cancion(id):
    return Tablatura.objects.filter(cancion=id)

@register.filter
def invitado_cancion(id):
    return Invitado.objects.filter(cancion=id)

@register.filter
def artista_cancion(id):
    return Artista.objects.filter(cancion=id)

@register.filter
def musico_artista(id):
    return Musico.objects.filter(artista=id)