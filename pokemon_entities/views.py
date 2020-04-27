import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "media/images/21.png"


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
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=10)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.pokemon_entities.all():
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
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    requested_pokemons = pokemon.pokemon_entities.all()
    next_evolutions = pokemon.next_evolutions.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in requested_pokemons:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.title_en,
            pokemon.photo.path,
        )

    pokemons_data = []
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

    if next_evolutions:
        next_evolutions_list = []
        pokemon_data['next_evolutions'] = next_evolutions_list
        for next_evolution in next_evolutions:
            next_evolution_dict = {"title_ru": next_evolution.title,
                                   "pokemon_id": next_evolution.id,
                                   "img_url": next_evolution.photo.path}
            next_evolutions_list.append(next_evolution_dict)

    pokemons_data.append(pokemon_data)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon,
                                                    'next_evolutions': next_evolutions,
                                                    })

