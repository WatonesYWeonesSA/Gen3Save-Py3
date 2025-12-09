from .pokemon_data import get_pokemon_data

def move_name(id):
    moves = get_pokemon_data("moves")
    return moves[id - 1]

def nature_name(id):
    natures = get_pokemon_data("natures")
    return natures[id]

# No implementado
def move_type(id): return ""