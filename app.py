from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

USERNAME = 'nawodya135@gmail.com'
PASSWORD = 'PASSWORD'
SIMILAR_ACCOUNT = 'chefsteps'

chrome_driver_path = '/home/nawodya_Dark/Third_party/chrome_Driver/chromedriver'

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get('https://www.instagram.com/')

    def login(self):
        time.sleep(4)
        username = self.driver.find_element_by_name('username')
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name('password')
        password.send_keys(PASSWORD)

        time.sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()

    def find_followers(self):
        time.sleep(4)
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)

        time.sleep(3)
        first_result = self.driver.find_element_by_class_name('-qQT3')
        first_result.click()

        time.sleep(4)
        followers = self.driver.find_element_by_partial_link_text(' followers')
        followers.click()

    def follow(self):
        fBody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 3: # scroll 5 times    
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(2)
            Follow_Button = self.driver.find_element_by_css_selector('.PZuss button')
            print(Follow_Button)
            for btn in Follow_Button:
                time.sleep(2)
                try:                        
                    btn.click()
                    
                except Exception as e:
                    time.sleep(1)
                    cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                    cancel.click()

            time.sleep(1)
            scroll += 1

        fList  = self.driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        print("fList len is {}".format(len(fList)))
        print("ended")





instagram = InstaFollower()
instagram.login()
instagram.find_followers()
time.sleep(4)
instagram.follow()











