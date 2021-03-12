import time
from pathlib import Path
from selenium import webdriver
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


# function to access the login page and log in
def botlogin (user, pwd):

    username = user
    password = pwd

    driver.get('https://www.instagram.com/') # instagram url
    time.sleep(2)

    userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
    userelement.clear()
    userelement.send_keys(username) # user insertion in 'user' element

    pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
    pwdelement.clear()
    pwdelement.send_keys(password) # password insertion in 'password' element
    pwdelement.send_keys(Keys.RETURN) # log in to page
    time.sleep(2)

    try:
        driver.find_element_by_xpath("//button[contains(text(),'Accetta')]").click() #change in Accept or Acepta or Accepte
    except:
        pass


#legge username e pwd
user = 'user'
pwd = 'pass'


botlogin(user,pwd)


