from colors import Colors
from system import System

class IOHandler:

	def __init__(self, system):
		# CFApp logo
		self.logo = '[' + Colors.YELLOW + 'cf' + Colors.BLUE +\
			'-' + Colors.RED + 'app' + Colors.WHITE + ']'

		self.system = system

	def print_logo(self):
		print(self.logo, end = ' ')

	def print_text(self, cmd):
		self.print_logo()
		print(cmd)

	def read_command(self, text):
		self.print_logo()
		return input(text).split()
