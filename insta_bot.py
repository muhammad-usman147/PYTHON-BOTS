from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class InstagramBot:
    def __init__(self,username,password):
        self.bot=webdriver.Firefox(executable_path='/home/admin1/Desktop/bot/geckodriver')
        self.username=username
        self.password=password
        self.bot.get('https://www.instagram.com/')
    def Login(self):
        bot=self.bot
        time.sleep(10)
        click_login=bot.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click()
        time.sleep(10)
        username=bot.find_element_by_name('username')
        username.send_keys(self.username)
        pasword=bot.find_element_by_name('password')
        pasword.send_keys(self.password)
        pasword.send_keys(Keys.RETURN)
        time.sleep(10)
        button=bot.find_element_by_class_name('HoLwm ')
        button.click()
    def GetLikes(self,tag):
        bot=self.bot
        bot.get('https://www.instagram.com/explore/tags/'+tag+'/')
        time.sleep(0)
        bot.execute_script('window.scroll(0,document.body.scrollHeight)')
        attrs=bot.find_elements_by_tag_name('a')
        links=[x.get_attribute('href') for x in attrs]
        for x in links:
            if '/p/' in x:
                bot.get(x)
                time.sleep(10)
                bot.find_element_by_class_name('u-__7').click()
                time.sleep(2)

x=InstagramBot('thanos_gauntlet','usman1234')
x.Login()
x.GetLikes('coding')
        