from .pokemon_data import get_pokemon_data

def species_name(id):
    names = get_pokemon_data("pokemon_names")
    if id>len(names):
        return ""
    return names[id - 1]

def kanto_id(id):
    if id <= 251:
        return id
    if id >= 413:
        return 201
    kanto = get_pokemon_data("kanto_ids")
    ix = id - 277
    if ix < len(kanto):
        return kanto[ix]
    return 0