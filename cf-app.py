import requests
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
from time import sleep
import clipboard
import os, sys
import subprocess, shlex
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display

PROJECT_PATH = os.path.dirname(__file__)
CURRENT_PATH = sys.argv[1]
SITE_URL = 'https://codeforces.com'
driver = ''

class Colors:
	YELLOW = '\033[0;93m'
	BLUE = '\033[0;34m' 
	RED = '\033[0;31m'
	WHITE = '\033[0;37m'
	GREEN = '\033[0;32m'

def print_cf_app():
	print('[' + Colors.YELLOW + 'cf' + Colors.BLUE + '-' + Colors.RED + 'app' + Colors.WHITE + ']', end = ' ')

def get_driver():
	print_cf_app()
	print('Initializing driver...')
	#return webdriver.Chrome()
	return webdriver.Firefox()

def get_username():
	fd = open(PROJECT_PATH + '/username')
	username = fd.readline()
	fd.close()
	return username

def get_password():
	fd = open(PROJECT_PATH + '/password')
	password = fd.readline()
	fd.close()
	return password

def login():
	print_cf_app()
	print('Loging in...')
	
	if check_if_page_exists('https://codeforces.com/enter?back=%2F'):	

		username = get_username()
		password = get_password()
		# username = ''
		# password = ''

		driver.find_element_by_name('handleOrEmail').send_keys(username)
		driver.find_element_by_name('password').send_keys(password)

		driver.find_element_by_name('remember').click()
		driver.find_element_by_class_name('submit').click()

		sleep(5)


def get_judge_verdict(task_id):

	last_subm = driver.find_elements_by_class_name('highlighted-row')[0]
	verdict = last_subm.find_elements_by_xpath('.//*')[8]
	
	counter = int(0)
	while True:
		move_up(1)
		print(last_subm.text)

		last_subm_text = last_subm.text

		if verdict.get_attribute('waiting') == 'false':
			move_up(1)
			print(last_subm.text, end = '\n\n')
			break	

		if last_subm_text != last_subm.text:
			counter = 0
		else:
			counter += 1

		if counter == 1000:
			driver.refresh()
			last_subm = driver.find_elements_by_class_name('highlighted-row')[0]
			verdict = last_subm.find_elements_by_xpath('.//*')[8]
			counter = 0
	
	print_cf_app()
	input("Type anything to continue...")


def submit(contest_url, contest_id, task_id):
	print_cf_app()
	print(f'Submitting task {task_id}:', end = '\n')

	task_url = get_task_url(contest_url, task_id)
	source_path = get_task_path(contest_id, task_id) + '/main.cpp'

	driver.get(task_url)
	select = Select(driver.find_element_by_name('programTypeId'))	
	select.select_by_index(4)
	driver.find_element_by_name('sourceFile').send_keys(source_path)
	driver.find_element_by_class_name('submit').click()

	sleep(5)

	if driver.current_url != contest_url + '/my':
		something_wrong('Cannot submit same file twice!')
	else:
		print('\n')
		get_judge_verdict(task_id)

def get_contest_url(contest_id):
	return SITE_URL + '/contest/' + contest_id

def get_task_url(contest_url, task_id):
	return contest_url + '/problem/' + task_id

def get_contest_path(contest_id):
	return CURRENT_PATH + '/' + contest_id

def get_task_path(contest_id, task_id):
	return get_contest_path(contest_id) + '/' + task_id

def make_directory(directory_path):
	if not os.path.exists(directory_path):
		os.mkdir(directory_path)

def check_if_page_exists(page_url):
	driver.get(page_url)
	if driver.current_url == page_url:
		return True
	return False

def get_number_of_tasks(contest_url, contest_path, contest_id):
	big_letters = map(chr, range(ord('A'), ord('Z') + 1))
	task_number = 0

	for task_id in big_letters:
		task_url = get_task_url(contest_url, task_id)

		if check_if_page_exists(task_url) == True:
			task_number += 1
			prepare_task(contest_url, contest_path, contest_id, task_id)
		else:
			break

	return task_number

def make_test(tests, current_id, fd):
	
	tests[current_id].click()
	fd.write(clipboard.paste())

def prepare_tests(task_url, task_path, task_id):
	tests_path = task_path + '/tests'
	make_directory(tests_path)
	
	driver.get(task_url)
	tests = driver.find_elements_by_class_name('input-output-copier')
	number_of_tests = int(len(tests) / 2)
	assert 2 * number_of_tests == len(tests) 

	test_count = int(0)
	while test_count < len(tests):
		
		test_id = int(test_count / 2)
		
		input_fd = open(tests_path + '/input' + str(test_id) + '.txt', 'w')
		output_fd = open(tests_path + '/output' + str(test_id) + '.txt', 'w')

		make_test(tests, test_count, input_fd)
		make_test(tests, test_count + 1, output_fd)

		test_count += 2
		print_cf_app()

		if test_count == len(tests):
			print(f'Downloading test {test_id + 1} / {number_of_tests}')
		else:
			print(f'Downloading test {test_id + 1} / {number_of_tests}', end = '\r')


def move_up(number_of_lines):
	print('\033[F' * int(number_of_lines), end = '')

def prepare_task(contest_url, contest_path, contest_id, task_id):
	if task_id == 'A':
		print_cf_app()
		print(f'Preparing task {task_id}')
	else:
		move_up(1)
		print(' ' * 40, end = '')
		move_up(1)
		print_cf_app()
		print(f'Preparing task {task_id}')

	task_url = get_task_url(contest_url, task_id)
	task_path = get_task_path(contest_id, task_id)
	make_directory(task_path)

	prepare_tests(task_url, task_path, task_id)

	if not os.path.exists(task_path + '/main.cpp'):
		subprocess.call(shlex.split('/' + PROJECT_PATH + '/make_main.sh ' + task_id + ' ' + task_path + '/main.cpp'))

	os.system('touch ' + task_path + '/' + task_id + '.in')
	os.system('touch ' + task_path + '/' + task_id + '.out')


def something_wrong(message):
	print_cf_app()
	print(message)
	print_cf_app()
	input('Type anything to continue...')


def prepare_contest(contest_id):
	print('')
	print_cf_app()
	print('Preparing contest...')
	contest_url = get_contest_url(contest_id)

	if check_if_page_exists(contest_url) == False:
		something_wrong('Invalid contest!')
		return ['', '']

	contest_path = get_contest_path(contest_id)
	make_directory(contest_path)

	number_of_tasks = get_number_of_tasks(contest_url, contest_path, contest_id) 

	return [contest_url, number_of_tasks]

def contest_exists(contest_id):
	if contest_id == '':
		something_wrong('Choose contest first')
		return False

	return True

def check(contest_id, task_id):
	contest_path = CURRENT_PATH + '/' + contest_id
	task_path = contest_path + '/' + task_id

	subprocess.call([PROJECT_PATH + '/checker.sh', task_id, task_path])

def valid_task(task_id, number_of_tasks):
	task_number = int(ord(task_id) - ord('A') + 1)
	if task_number <= number_of_tasks and task_number > 0:
		return True

	something_wrong('Invalid task!')	
	return False

def main():
	display = Display(visible = 0, size = (1360, 760))
	#display.start()

	os.system('clear')
	
	global driver
	driver = get_driver()
	print_cf_app()
	print('Accessing https://codeforces.com')
	driver.get(SITE_URL)
	login()

	contest_url = ''
	contest_id = ''
	number_of_tasks = int(0)

	while True:
		os.system('clear')
		print_cf_app()
		command = input('Enter: ').split()

		if command[0] == 'quit':
			break

		elif command[0] == 'submit':
			if contest_exists(contest_id) and valid_task(command[1], number_of_tasks):
				submit(contest_url, contest_id, command[1])	
		
		elif command[0] == 'contest':
			contest_id = command[1]
			contest_url, number_of_tasks = prepare_contest(command[1])

		elif command[0] == 'check':
			if contest_exists(contest_id) and valid_task(command[1], number_of_tasks):
				check(contest_id, command[1])
				print_cf_app()
				input('Type anything to continue...')

		else:
			something_wrong('Invalid command!')	
		

	driver.quit()
	#display.stop()
	os.remove(CURRENT_PATH + '/geckodriver.log')
	os.system('clear')


if __name__ == '__main__':
	main()

