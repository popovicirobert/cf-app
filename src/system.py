import os, sys


class System:

	def __init__(self):
		
		self.SRC_PATH = os.path.dirname(__file__)
		self.ROOT_PATH = os.path.abspath(os.path.join(self.SRC_PATH, os.pardir))
		self.SH_PATH = os.path.join(self.ROOT_PATH, 'sh')

		self.USERNAME_PATH = os.path.join(os.path.join(self.ROOT_PATH, 'info'), 'username')
		self.PASSWORD_PATH = os.path.join(os.path.join(self.ROOT_PATH, 'info'), 'password')

		self.CONTEST_PATH = sys.argv[1]



	def ask_for_username(self, io):
		username = io.read_command('Username: ')
		return username[0]


	def get_username(self, io):
		if os.path.exists(self.USERNAME_PATH)
			with open(self.USERNAME_PATH, 'r') as fd:
				username = fd.readline()

		else:
			username = self.ask_for_username(io)

			with open(self.USERNAME_PATH, 'w') as fd:
				fd.write(username)

		return username


	def ask_for_password(self, io):
		password = io.read_command('Password: ')
		return password[0]

	def get_password(self, io):
		if os.path.exists(self.PASSWORD_PATH)
			with open(self.PASSWORD_PATH, 'r') as fd:
				password = fd.readline()

		else:
			password = self.ask_for_password(io)

			with open(self.PASSWORD_PATH, 'w') as fd:
				fd.write(password)

		return password




	def clear_screen(self):
		os.system('clear')

	def remove(self, file):
		if os.path.isfile(file):
			os.system(f'rm {file}')
