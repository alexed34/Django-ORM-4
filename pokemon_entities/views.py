import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
<<<<<<< HEAD
        for pokemon_entity in pokemon.pokemon_entities.all():
=======
        for pokemon_entity in PokemonEntity.objects.filter(choose_pokemon=pokemon):
>>>>>>> parent of 98b276e... 32 шаг
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title_en,
                pokemon.photo.path)
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemons(request, pokemon_id):
<<<<<<< HEAD
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    requested_pokemons = pokemon.pokemon_entities.all()
    next_evolutions = pokemon.next_evolutions.all()
=======
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemons = PokemonEntity.objects.filter(choose_pokemon=pokemon)

            try:
                next_evolution = Pokemon.objects.get(previous_evolution=pokemon)
            except:
                next_evolution = None
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
>>>>>>> parent of 98b276e... 32 шаг

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in requested_pokemons:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.title_en,
            pokemon.photo.path,
        )

    pokemons_data_json = []
    pokemon_data = {"pokemon_id": pokemon.id,
                    "title_ru": pokemon.title,
                    "title_en": pokemon.title_en,
                    "title_jp": pokemon.title_jp,
                    "description": pokemon.description,
                    "img_url": pokemon.photo.path,
                    }
    if pokemon.previous_evolution:
        previous_evolution_dict = {"title_ru": pokemon.previous_evolution.title,
                                   "pokemon_id": pokemon.previous_evolution.id,
                                   "img_url": pokemon.previous_evolution.photo.path}
        pokemon_data['previous_evolution'] = previous_evolution_dict

    if next_evolution:
        next_evolution_dict = {"title_ru": next_evolution.title,
                               "pokemon_id": next_evolution.id,
                               "img_url": next_evolution.photo.path}
        pokemon_data['next_evolution'] = next_evolution_dict

    pokemons_data_json.append(pokemon_data)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon,
                                                    'next_evolution': next_evolution,
                                                    })
