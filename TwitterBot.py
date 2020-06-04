# twitter bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from DataFile import *
from time import sleep
import os
import random

#temp login details
username = '@gmail.com'
password = ''
img_path = 'image'
tweet_text = 'text'
#
def rand_sleep(min = 0):
    return sleep(min + random.randint(1, 6))


class TwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except ValueError as msg:
            print('NoSuchElementException' + str(msg))
            return False
        return True

     # function logs into account using details in "secrets.py"
    
    #clicks a button identified by xpath
    def clicker(self, xpath):
        rand_sleep(1)
        self.check_exists_by_xpath(xpath)
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()

    #sends string to a entity defined by xpath
    def sender(self,xpath, obj):
        rand_sleep(1)
        self.check_exists_by_xpath(xpath)
        obj = self.driver.find_element_by_xpath(xpath)
        sleep(2)
        obj.send_keys(obj)


    def login(self):

        self.driver.get("https://twitter.com/login")
        rand_sleep()

        xpath = '//*[@name="session[username_or_email]"]'
        user_in = self.driver.find_element_by_xpath(xpath)
        user_in.send_keys(username)
        rand_sleep()

        xpath = '//*[@name="session[password]"]'
        pass_in = self.driver.find_element_by_xpath(xpath)
        pass_in.send_keys(password)

        pass_in.send_keys(Keys.ENTER)
        sleep(2)

        url_not_logged_in = 'https://twitter.com/login/error?username_or_email=username&redirect_after_login=%2F'

        if self.driver.current_url == url_not_logged_in:
            print("Username or Password are incorrect")
            exit()
     
    #tweets an image an text using the values provided   
    def tweeter(self):

        self.driver.refresh()
        # new tweet button
        new_tweet_btn = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
        self.clicker(new_tweet_btn)

        # Tweeting Image
        tweet_img_field = '//*[@type="file"]'
        self.sender(tweet_img_field, img_path)
        # Tweeting text
        tweet_text_field = '//div[@aria-label="Tweet text"]'
        self.sender(tweet_text_field, tweet_text)

        # clicking tweet send button
        tweet_btn = '//div[@data-testid="tweetButton"]'
        self.clicker(tweet_btn)
        
    #not working currently
    def accept_follow_requests(self):

        self.driver.refresh()
        more_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div/div/div')
        more_btn.click()

        opt_follow_req = self.driver.find_element_by_xpath(
              '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/a/div/div[1]')
        opt_follow_req.click()

        # accept buttons
        accept_btn = self.driver.find_elements_by_xpath(
              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/section/div/div/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div')
        accept_btn[0].click()

bot = TwitterBot()
bot.login()
