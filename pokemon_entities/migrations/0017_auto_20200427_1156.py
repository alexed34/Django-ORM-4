# Generated by Django 2.2.3 on 2020-04-27 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20200423_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonentity',
            name='pokemon_model',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.Pokemon', verbose_name='Выбрать покемона'),
        ),
    ]
