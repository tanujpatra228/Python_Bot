from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        print('waiting to load : login page')
        time.sleep(15)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        print(email)
        print(password)
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        print('login complete...')

    def search_twitter(self, term):
        print('waiting to load : profile page')
        time.sleep(15)
        bot = self.bot
        # search_box = bot.find_element_by_tag_name('input')
        search_box = bot.find_element_by_xpath('//input[@placeholder="Search Twitter"][@type="text"]')
        print(search_box)
        search_box.send_keys(term)
        search_box.send_keys(Keys.ENTER)
        print('waiting to load :' + term)
        time.sleep(15)
        for i in range(1, 3):
            # bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            bot.execute_script('window.scrollTo(0, 500)')
            time.sleep(5)
            like_btn = bot.find_element_by_xpath('//div[@data-testid="like"]')
            print(like_btn)
            like_btn.click()
            print('Liked...')
            time.sleep(5)


your_username = ''
your_password = ''
search_phase = '#wordpress'

tp = TwitterBot(your_username, your_password)
tp.login()
time.sleep(5)
tp.search_twitter(search_phase)
