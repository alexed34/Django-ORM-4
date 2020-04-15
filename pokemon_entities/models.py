from django.db import models
from django.db.models import DateTimeField, IntegerField


class Pokemon(models.Model):
    title = models.CharField(max_length=200, default=" ", verbose_name='Имя на русском')
    title_en = models.CharField(max_length=200, default=" ", verbose_name='Имя на английском')
    title_jp = models.CharField(max_length=200, default=" ", verbose_name='Имя на японском')
    photo = models.ImageField(upload_to='images', null=True, verbose_name='Загрузить фото')
    description = models.CharField(max_length=2000, default=" ", verbose_name='Описание')
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolution',
                                           on_delete=models.SET_NULL)

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    title = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Выбрать покемона')
    lat = models.FloatField(null=True, verbose_name='Широта')
    lon = models.FloatField(null=True, verbose_name='Долгота')
    appeared_at = DateTimeField(null=True, verbose_name='Время появления')
    disappeared_at = DateTimeField(null=True, verbose_name='Время исчезновения')
    level = IntegerField(null=True, verbose_name='Уровень')
    health = IntegerField(null=True, verbose_name='Здоровье')
    strength = IntegerField(null=True, verbose_name='Сила')
    defence = IntegerField(null=True, verbose_name='Защита')
    stamina = IntegerField(null=True, verbose_name='Выносливость')
