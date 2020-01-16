# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description

		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None

	def __str__(self):
		display_string = ''
		display_string += f'\n----------------\n'
		display_string += f'\n{self.name}\n'
		display_string += f'\n{self.description}\n'
		display_string += f'{self.get_exits_string()}'
		return display_string

	def get_room_in_direction(self, direction):
		if direction == 'n':
			return self.n_to
		elif direction == 's':
			return self.s_to
		elif direction == 'e':
			return self.e_to
		elif direction == 'w':
			return self.w_to
		else:
			return 

	def get_exits(self):
		exits = []
		if self.n_to:
			exits.append('n')
		if self.s_to:
			exits.append('s')
		if self.e_to:
			exits.append('e')
		if self.w_to:
			exits.append('w')
		return exits

	def get_exits_string(self):
		return f"Exits: {', '.join(self.get_exits())}"