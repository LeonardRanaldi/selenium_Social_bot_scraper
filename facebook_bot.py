from pathlib import Path
import time
from selenium import webdriver
import platform

mySystem = platform.system() # you can replace with Linux, Darwin,Windows

# in this script geckodriver is used and the path is selected according to the OS
if mySystem == 'Linux':

    mySystem = 'clear'
    way = Path('./geckodriver-v0.26.0-linux64') # path to the file
    geckoFile = way / 'geckodriver' # way to geckodriver

elif mySystem == 'Windows':
    mySystem = 'cls'
    way = Path('geckodriver/windows') # path to the file
    geckoFile = way / 'geckodriver.exe' # way to geckodriver

elif mySystem == 'Darwin':
    mySystem = 'clear' #https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-macos.tar.gz
    way = Path('./geckodriver-v0.28.0-macos') # path to the file
    geckoFile = way / 'geckodriver' # way to geckodriver

driver = webdriver.Firefox(executable_path=f'{geckoFile}')

# if you want to use chromedriver you have to comment out these recipes and uncomment this one (according to the OS)
#driver = webdriver.Chrome("/usr/local/bin/chromedriver")


def login(email, password):
    driver.get("http://facebook.com")
    driver.maximize_window()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_id('loginbutton').click()
    time.sleep(2)
    print('You Are Logged!!')



EMAIL = 'user'
PASSWORD = 'pass'

login(EMAIL,PASSWORD)





