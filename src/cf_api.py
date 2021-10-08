
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
# from system import System

DEBUG = True


class CFApi:

	def __init__(self, system, io):

		# after debugging is over, switch to headless mode
		self.driver = webdriver.Chrome()

		self.SITE_URL = 'https://codeforces.com'
		self.LOGIN_URL = 'https://codeforces.com/enter?back=%2F'

		self.system = system
		self.io = io
		self.sleep_time = 100

	def load_page(self, url):
		self.driver.get(url)

		while self.driver.current_url != url:
			self.system.sleep(sleep_time)

	def click_elem(self, elem):
		action = self.ActionChains(self.driver)
		action.move_to_element(elem).click().perform()


	def send_keys_elem(self, elem, text):
		action = self.ActionChains(self.driver)
		action.move_to_element(elem).send_keys(text).perform()

		WebDriverWait(self.browser).until(lambda d: elem.get_attribute('value') == text)

		
	def login(self):
		 self.load_page(self.LOGIN_URL)

		 username = self.system.get_username(self.io)
		 password = self.system.get_password(self.io)

		 username_el = WebDriverWait(driver).until(lambda d: d.find_element_by_name("handleOrEmail"))
		 password_el = WebDriverWait(driver).until(lambda d: d.find_element_by_name("password"))





	def __del__(self):
		self.driver.quit()