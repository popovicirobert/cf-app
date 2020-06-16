try:
	import requests
	from selenium import webdriver 
	from selenium.webdriver.firefox.options import Options 
	from time import sleep
	import clipboard
	import os, sys
	import subprocess, shlex
	from selenium.webdriver.support.ui import Select
	from pyvirtualdisplay import Display
except:
	import install_requirements

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

def get_driver():
	print("Initializing driver...")
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

def login(driver):
	print("Loging in...")
	driver.get('http://codeforces.com/enter?back=%2F')
	
	username = get_username()
	password = get_password()
	# username = ''
	# password = ''

	driver.find_element_by_name('handleOrEmail').send_keys(username)
	driver.find_element_by_name('password').send_keys(password)

	driver.find_element_by_name('remember').click()
	driver.find_element_by_class_name('submit').click()

	sleep(5)

def submit(contest_url, contest_id, task_id):
	print(f'Submiting task {task_id}...')
	task_url = get_task_url(contest_url, task_id)
	source_path = get_task_path(contest_id, task_id) + '/main.cpp'

	driver.get(task_url)
	select = Select(driver.find_element_by_name('programTypeId'))	
	select.select_by_index(4)
	driver.find_element_by_name('sourceFile').send_keys(source_path)
	driver.find_element_by_class_name('submit').click()

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

def get_number_of_tasks(contest_url, contest_id):
	big_letters = map(chr, range(ord('A'), ord('Z') + 1))
	task_number = 0

	for task_id in big_letters:
		task_url = get_task_url(contest_url, task_id)

		if check_if_page_exists(task_url) == True:
			task_number += 1
		else:
			break

	return task_number

def make_test(tests, current_id, fd):
	tests[current_id].click()
	fd.write(clipboard.paste())

def prepare_tests(task_url, task_path, task_id):
	print(f'Downloading tests for task {task_id}')
	tests_path = task_path + '/tests'
	make_directory(tests_path)
	
	driver.get(task_url)
	tests = driver.find_elements_by_class_name('input-output-copier')
	assert len(tests) % 2 == 0

	test_count = int(0)
	while test_count < len(tests):
		
		test_id = int(test_count / 2)
		
		input_fd = open(tests_path + '/input' + str(test_id) + '.txt', 'w')
		output_fd = open(tests_path + '/output' + str(test_id) + '.txt', 'w')

		make_test(tests, test_count, input_fd)
		make_test(tests, test_count + 1, output_fd)

		test_count += 2
	

def prepare_task(contest_url, contest_path, contest_id, task_id):
	print(f'Preparing task {task_id}')
	task_url = get_task_url(contest_url, task_id)
	task_path = get_task_path(contest_id, task_id)
	make_directory(task_path)

	prepare_tests(task_url, task_path, task_id)

	if not os.path.exists(task_path + '/main.cpp'):
		subprocess.call(shlex.split('/' + PROJECT_PATH + '/make_main.sh ' + task_id + ' ' + task_path + '/main.cpp'))

	os.system('touch ' + task_path + '/' + task_id + '.in')
	os.system('touch ' + task_path + '/' + task_id + '.out')


def prepare_contest(contest_id):
	print('Preparing contest...')
	contest_url = get_contest_url(contest_id)

	contest_path = get_contest_path(contest_id)
	make_directory(contest_path)

	number_of_tasks = get_number_of_tasks(contest_url, contest_id) 
	big_letters = map(chr, range(ord('A'), ord('A') + number_of_tasks))

	for task_id in big_letters:
		prepare_task(contest_url, contest_path, contest_id, task_id)

	return contest_url

def contest_exists(contest_id):
	if contest_id == '':
		print('Choose contest first!')
		return False

	return True

def check(contest_id, task_id):
	contest_path = CURRENT_PATH + '/' + contest_id
	task_path = contest_path + '/' + task_id

	subprocess.call([PROJECT_PATH + '/checker.sh', task_id, task_path])


def main():
	display = Display(visible = 0, size = (1360, 760))
	display.start()
	
	global driver
	driver = get_driver()
	driver.get(SITE_URL)
	login(driver)

	contest_url = ''
	contest_id = ''

	while True:
		command = input('Enter: ').split()

		if command[0] == 'quit':
			break

		elif command[0] == 'submit':
			if contest_exists(contest_id):
				submit(contest_url, contest_id, command[1])	
		
		elif command[0] == 'contest':
			contest_id = command[1]
			contest_url = prepare_contest(command[1])

		elif command[0] == 'check':
			if contest_exists(contest_id):
				check(contest_id, command[1])
		
		print('\n')

	driver.quit()
	display.stop()
	os.remove(sys.argv[1] + '/geckodriver.log')


if __name__ == '__main__':
	main()

