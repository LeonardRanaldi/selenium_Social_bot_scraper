from selenium import webdriver
from pathlib import Path
import time
from selenium.webdriver.common.keys import Keys
import platform

mySystem = platform.system() # you can replace with Linux, Darwin,Windows

#in this script geckodriver is used and the path is selected according to the OS.
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



def login_twitter (user, pwd):

    username = user
    password = pwd

    driver.get('https://twitter.com/login') # instagram url
    time.sleep(2)

    userelement = driver.find_element_by_css_selector("input[name='session[username_or_email]']") # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element

    time.sleep(1)
    pwdelement = driver.find_element_by_css_selector("input[name='session[password]']") # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    time.sleep(2)
    print('You Are Logged!!')

email = 'user'
pwd = 'pass'


login_twitter(email, pwd)
