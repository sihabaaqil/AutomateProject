from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import warnings
import emoji
from emoji import emojize
import demoji

ROOT_DIR = os.path.abspath(os.curdir)
ser= Service(ROOT_DIR+'\chromedriver.exe')
gd = (ROOT_DIR+'\chromedriver.exe')
# print(ROOT_DIR+'\chromedriver.exe')
driver = webdriver.Chrome(service= ser)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Ayisha"'

# Replace the below string with your own message
string = "Baby"

x_arg = '//span[contains(@title,' + target + ')]'
# print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
# print("click")
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
# print("ele pre" + inp_xpath)
for i in range(1000):
	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)