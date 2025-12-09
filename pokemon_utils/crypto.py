from operator import xor
import struct

# Decodifica el contenido de un string del formato del SAV a ASCII
def read_string(text):
    # tabla de caracteres usados para decodificar
    chars = "0123456789!?.-         ,  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # string acumulador
    ret = ""
    
    # recorre cada elemento del texto codificado
    for i in text:
        # convierte el valor a numero y aplica el offset usado por el formato
        c = int(i) - 161
        
        # si el codigo esta fuera de rango, agrega espacio
        if c < 0 or c > len(chars):
            ret += " "
        else:
            # si esta dentro del rango, toma el caracter correspondiente
            ret += chars[c]
    
    # limpia espacios sobrantes y retorna
    return ret.strip()

def decrypt_subsection(data, key):
    # revisa que el bloque tenga el tamano esperado
    if len(data) != 12:
        return []
    
    # extrae los primeros 4 bytes como entero y aplica xor con la llave
    a = xor(struct.unpack('<I', data[0:4])[0], key)
    
    # extrae los siguientes 4 bytes y aplica xor
    b = xor(struct.unpack('<I', data[4:8])[0], key)
    
    # extrae los ultimos 4 bytes y aplica xor
    c = xor(struct.unpack('<I', data[8:12])[0], key)
    
    # empaqueta nuevamente los tres enteros en binario
    return struct.pack('<III', a, b, c)
