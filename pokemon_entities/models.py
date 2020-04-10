from django.db import models
from django.db.models import DateTimeField, IntegerField


class Pokemon(models.Model):
    title = models.CharField(max_length=200, default=" ")
    photo = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    appeared_at = DateTimeField(null=True)
    disappeared_at = DateTimeField(null=True)
    level = IntegerField(null=True)
    health = IntegerField(null=True)
    strength = IntegerField(null=True)
    defence = IntegerField(null=True)
    stamina = IntegerField(null=True)
