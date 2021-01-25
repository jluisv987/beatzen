from django.urls import path
from . import views

urlpatterns= [
    path('',views.index),
    path('buscar/',views.buscar),
    path('busqueda/',views.busqueda),
    path('artista/<artista_id>/',views.artista,name = "artista"),
    path('cancion/<cancion_id>/',views.cancion,name = "cancion"),
    path('album/<album_id>/',views.album,name = "album"),
]
