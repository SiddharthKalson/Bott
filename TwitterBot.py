# twitter bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DataFile import username, password, image_path, tweet_text
from time import sleep
import os
import random

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

    def tweeter(self):

        self.driver.refresh()
        ###########Standard way for performing aciton############
        #                   declaring sleep time                                                       #
        #                   assigning element value (must be non dynamic)         #
        #                   check element for existence                                         #
        #                   assign variable to element                                            #
        #                   click or send keys to element                                       #
        #################################################
        # new tweet button
        rand_sleep(1)
        xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
        self.check_exists_by_xpath(xpath)
        new_tweet_btn = self.driver.find_element_by_xpath(xpath)
        new_tweet_btn.click()

        # Tweeting Image
        rand_sleep(1)
        xpath = '//*[@type="file"]'
        self.check_exists_by_xpath(xpath)
        tweet_img = self.driver.find_element_by_xpath(xpath)
        sleep(2)
        tweet_img.send_keys(image_path)

        # Tweeting text
        rand_sleep(1)
        xpath = '//div[@aria-label="Tweet text"]'
        self.check_exists_by_xpath(xpath)
        tweet_text = self.driver.find_element_by_xpath(xpath)
        sleep(2)
        tweet_text.send_keys(tweet_text)

        # clicking tweet send button
        rand_sleep(1)
        xpath = '//div[@data-testid="tweetButton"]'
        self.check_exists_by_xpath(xpath)
        tweet_btn = self.driver.find_element_by_xpath(xpath)
        sleep(2)
        tweet_btn.click()

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
