from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=50)
    biografia = models.CharField(max_length=1000)
    pagina = models.CharField(max_length=100)
    imagen = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre=models.CharField(max_length=50)
    estudio=models.CharField(max_length=50)
    ano_lanzamiento=models.DateField()
    no_pistas=models.IntegerField()
    imagen = models.ImageField(null=True,blank=True)
    artista = models.ForeignKey(Artista,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.nombre

class Musico(models.Model):
    nombre = models.CharField(max_length=50)
    instrumento = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    class Meta:
        verbose_name_plural = "Canciones"
    nombre=models.CharField(max_length=50)
    duracion = models.CharField(max_length=10)
    no_cancion = models.IntegerField()
    url = models.CharField(max_length=100)
    #musico = models.ForeignKey(Musico,null=True,on_delete=models.SET_NULL)
    artista = models.ForeignKey(Artista,null=True,on_delete=models.SET_NULL)
    album = models.ForeignKey(Album,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.nombre

class Tablatura(models.Model):
    cancion_instrumento = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    fecha = models.DateField()
    traductor = models.CharField(max_length=50)
    email_traductor = models.CharField(max_length=50)
    imagen = models.ImageField(null=True,blank=True)
    cancion = models.ForeignKey(Cancion,null=True,on_delete=models.SET_NULL)
def __str__(self):
        return self.cancion_instrumento

class Invitado(models.Model):
    musico_cancion = models.CharField(max_length=50)
    cancion = models.ForeignKey(Cancion,null=True,on_delete=models.SET_NULL)
    musico = models.ForeignKey(Musico,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.musico_cancion