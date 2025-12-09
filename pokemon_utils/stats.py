import struct

def get_ivs(value):
    iv = {}
    bitstring = str(bin(value)[2:])[::-1] + '00000000000000000000000000000000'
    iv['hp'] = int(bitstring[0:5][::-1], 2)
    iv['attack'] = int(bitstring[5:10][::-1], 2)
    iv['defence'] = int(bitstring[10:15][::-1], 2)
    iv['speed'] = int(bitstring[15:20][::-1], 2)
    iv['spatk'] = int(bitstring[20:25][::-1], 2)
    iv['spdef'] = int(bitstring[25:30][::-1], 2)
    return iv

def get_evs(section):
    ev = {}
    ev['hp'] = int(struct.unpack('<B', section[0:1])[0])
    ev['attack'] = int(struct.unpack('<B', section[1:2])[0])
    ev['defence'] = int(struct.unpack('<B', section[2:3])[0])
    ev['speed'] = int(struct.unpack('<B', section[3:4])[0])
    ev['spatk'] = int(struct.unpack('<B', section[4:5])[0])
    ev['spdef'] = int(struct.unpack('<B', section[5:6])[0])
    ev['cool'] = int(struct.unpack('<B', section[6:7])[0])
    ev['beauty'] = int(struct.unpack('<B', section[7:8])[0])
    ev['cute'] = int(struct.unpack('<B', section[8:9])[0])
    ev['smart'] = int(struct.unpack('<B', section[9:10])[0])
    ev['tough'] = int(struct.unpack('<B', section[10:11])[0])
    ev['feel'] = int(struct.unpack('<B', section[11:12])[0])
    return ev