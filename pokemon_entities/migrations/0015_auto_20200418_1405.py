# Generated by Django 2.2.3 on 2020-04-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20200418_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Choose_pokemon',
            new_name='choose_pokemon',
        ),
    ]
