import json
import importlib.resources as res

# Solo importa la data del json para hacer mas legible el codigo, el json es la fuente de datos.
# Mas adelante se debe migrar a SQLite para tener mas orden.
def get_pokemon_data(datablock: str):
    with res.open_text(__package__, "pokemon_data.json") as f:
        data = json.load(f)

    return data[datablock]