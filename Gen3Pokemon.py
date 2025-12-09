import struct
from .pokemon_utils import crypto, stats, taxonomy, level_manage, misc
from operator import xor

class Gen3Pokemon:
	def __init__(self, pkm):
		orders = ['GAEM', 'GAME', 'GEAM', 'GEMA', 'GMAE', 'GMEA', 'AGEM', 'AGME', 'AEGM', 'AEMG', 'AMGE', 'AMEG', 'EGAM', 'EGMA', 'EAGM', 'EAMG', 'EMGA', 'EMAG', 'MGAE', 'MGEA', 'MAGE', 'MAEG', 'MEGA', 'MEAG']
		self.name = crypto.read_string(pkm[8:18])
		self.data = pkm
		trainer = crypto.read_string(pkm[20:27])
		if trainer == '' and self.name == '':
			return None
		self.personality = struct.unpack('<I', pkm[0:4])[0]
		self.trainer = {'id': struct.unpack('<I', pkm[4:8])[0], 'name': trainer}
		key = xor(self.trainer['id'], self.personality)

		data = pkm[32:]
		order = self.personality % 24
		orderstring = orders[order]
		sections = {}
		for i in range(0, 4):
			section = orderstring[i]
			sectiondata = data[(i * 12):((i + 1) * 12)]
			decr = crypto.decrypt_subsection(sectiondata, key)
			sections[section] = decr
		decrypted = [sections['G'], sections['A'], sections['E'], sections['M']]
		self.data = self.data[0:32] + b''.join(decrypted)
		self.species = {'id': int(struct.unpack('<H', sections['G'][0:2])[0])}
		self.species['name'] = taxonomy.species_name(self.species['id'])
		self.species['nid'] = taxonomy.kanto_id(self.species['id'])
		self.exp = int(struct.unpack('<I', sections['G'][4:8])[0])
		self.expgroup = level_manage.exp_group(self.species['id'])
		self.level = level_manage.level(self.expgroup, self.exp)
		if self.name == '':
			self.name = self.species['name'].upper()

		moves = []
		for i in range(0, 4):
			item = {}
			item['id'] = int(struct.unpack('<H', sections['A'][(i * 2):((i + 1) * 2)])[0])
			if item['id'] == 0:
				continue
			item['name'] = misc.move_name(item['id'])
			item['pp'] = int(struct.unpack('<B', sections['A'][(i + 8):(i + 9)])[0])
			moves.append(item)
		self.moves = moves
		self.nature = misc.nature_name(self.personality % 25)
		self.ivs = stats.get_ivs(int(struct.unpack('<I', sections['M'][4:8])[0]))
		self.evs = stats.get_evs(sections['E'])