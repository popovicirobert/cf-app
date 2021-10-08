from cf_api import CfApi
from io_handler import IOHandler
from commands import Commands
from system import System


class CFApp:

	def __init__(self):
		self.system = System()
		self.io = IOHandler(self.system)
		self.cf_api = CfApi(self.system, self.io)

		self.running = False

	def quit_app(self):
		self.running = False

	def submit_task(self, cmd):
		pass

	def load_contest(self, cmd):
		pass

	def check_task(self, cmd):
		pass

	def run(self):

		self.cf_api.login()

		self.running = True
		sleep_time = 50

		while self.running:

			# don't forget to release the CPU once in a while
			system.sleep(sleep_time)

			self.system.clear_screen()
			cmd = self.io.read_command('Enter: ')

			if cmd[0] == COMMANDS.QUIT:
				self.quit_app()

			elif cmd[0] == COMMANDS.SUBMIT:
				self.submit_problem(cmd)

			elif cmd[0] == COMMANDS.CONTEST
				self.load_contest(cmd)

			elif cmd[0] == COMMANDS.CHECK:
				self.check_problem(cmd)

			else:
				self.io.print_text("Invalid command")
