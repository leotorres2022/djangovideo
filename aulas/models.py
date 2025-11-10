from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.instrument}"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    
    def __str__(self):
        # Mostrar el nombre del álbum y el artista (llama a Musician.__str__)
        return f"{self.name} by {self.artist}"

    def __unicode__(self):
        # Mantener compatibilidad conceptual con Python 2/3 si es necesario
        return self.__str__()
    