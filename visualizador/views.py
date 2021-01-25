from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'visualizador/index.html')

def buscar(request):
    return render(request,'visualizador/buscar.html')

def busqueda(request):
    if request.method=="POST":
        query = request.POST.get('query')
        context ={}     
        seleccion = request.POST.get('seleccion')    
        if seleccion == 'Artista':
            busqueda = Artista.objects.filter(nombre__icontains=query)
        elif seleccion == 'Album':
            busqueda = Album.objects.filter(nombre__icontains=query)
        elif seleccion == 'Canción':
            busqueda = Cancion.objects.filter(nombre__icontains=query)

        return render(request,'visualizador/busqueda.html',{'busqueda':busqueda})

def artista(request,artista_id):
    artista= Artista.objects.filter(id=artista_id);
    return render(request,'visualizador/artista.html',{'artista':artista})

def cancion(request,cancion_id):
    cancion= Cancion.objects.filter(id=cancion_id);
    return render(request,'visualizador/cancion.html',{'cancion':cancion})

def album(request,album_id):
    album= Album.objects.filter(id=album_id);
    return render(request,'visualizador/album.html',{'album':album})