# Generated by Django 2.2.3 on 2020-04-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20200418_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='title',
            new_name='Choose_pokemon',
        ),
    ]
