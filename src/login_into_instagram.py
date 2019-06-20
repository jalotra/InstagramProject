from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.common.exceptions import NoSuchElementException
import time
import requests

INSTAGRAM_HOMEPAGE_URL = str("https://www.instagram.com")

class LoginInstagram():
    def __init__(self, username = None, password = None):
        self.instagramLink = INSTAGRAM_HOMEPAGE_URL 
        self.username = username 
        self.password = password
        self.sleepTime = 2
        self.driver = webdriver.Firefox()

    # def __str__(self):
    #     return  'Instagram Model to get more followers and using' + str(self.webdriver_ask()) + 'Webdriver Backend '

    ''' 
    Capability to add Chrome Webdriver as well'''
    # def webdriver_ask(self):
    #     webdriverName = input('Which Webdriver Backend do you want to use? \n'
    #         'The possible choices can be \n 1.Chrome \n 2.Firefox \n')
    #     if webdriverName.lower() == 'chrome':
    #         webdriverName = webdriverName[0].upper() + webdriverName[1:]
    #     elif webdriverName.lower() == 'firefox':
    #         webdriverName = webdriverName[0].upper() + webdriverName[1:]
    #     else:
    #         print('No Mentioned Backend is Possible')
    #         webdriverName = None
    #     return webdriverName


    def open_homepage(self):
        self.driver.get(self.instagramLink)

    def close_browser(self):
        self.driver.close()
            
    def login_in_instagram(self):
        #xpathfortheloginpage = "//a[@href'/accounts/login/?source=auth_switcher']"
        #xpathforusername = "//input[@name = 'username' ]"
        #xpathforpassword = "//input[@name = 'password']"
        # loginButton = self.driver.find_element(By.XPATH , "//a[contains(@href,'/accounts/login/?source=auth_switcher/')]")
        #this thing 
        loginURL = self.instagramLink + '/accounts/login/?source=auth_switcher'
        self.driver.get(loginURL)
        time.sleep(self.sleepTime)
        try:
            usernameButton = self.driver.find_element(By.XPATH , "//input[@name = 'username']")
            usernameButton.send_keys(self.username)
            passwordButton = self.driver.find_element(By.XPATH, "//input[@name = 'password']")
            passwordButton.send_keys(self.password)
            passwordButton.send_keys(Keys.RETURN)
            time.sleep(self.sleepTime)
        except:
            if requests.get(loginURL).status_code != 200:
                print('NOT ABLE TO OPEN THE LOGIN PAGE')

            
    def status_generator(self):
        #xpath for password is wrong = "//p[@id ='slfErrorAlert']"
        try:
            self.driver.find_element(By.XPATH, "//p[@id ='slfErrorAlert']")
            passwordWrongElement = self.driver.find_element(By.XPATH, "//p[@id = 'slfErrorAlert']")
            print(passwordWrongElement.text.upper())
        except NoSuchElementException:
            print('HAVE A GOOD DAY YOU JUST ENTERED INSTAGRAM')



if __name__ == "__main__":
    Object = LoginInstagram('', '')
    # Object.__str__()
    try:
        Object.login_in_instagram()
        Object.status_generator()
    except KeyboardInterrupt:
        Object.close_browser()  
    # Object.close_browser()
    
