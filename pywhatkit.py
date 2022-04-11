import pywhatkit
import os
from selenium.webdriver.chrome.service import Service
# pywhatkit.sendwhatmsg("+919944380786","Geeks For Geeks!",18, 30)
ROOT_DIR = os.path.abspath(os.curdir)
ser= Service(ROOT_DIR+'\chromedriver.exe')
gd = (ROOT_DIR+'\chromedriver.exe')
driver = webdriver.Chrome(service= ser)
pywhatkit.add_