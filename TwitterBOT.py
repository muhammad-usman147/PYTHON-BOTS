from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from python_generate_password import password
import time
''' class Botter:
    def __init__(self,search):
        self.search=search
        self.bot = webdriver.Firefox(executable_path='/home/admin1/Desktop/bot/geckodriver')
    def Login(self):
        bot=self.bot
        bot.get('https://www.google.com')
        time.sleep(7)
        clicker=bot.find_element_by_name('q')
        clicker.send_keys(self.search)
        clicker.send_keys(Keys.RETURN)  '''
class TwitterBot():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox(executable_path='/home/admin1/Desktop/bot/geckodriver')
    def Sleeper(self):
        time.sleep(4)
    def Login(self):
        bot=self.bot
        
        bot.get('https://www.twitter.com')
        self.Sleeper()
        bot.find_element_by_class_name('u-floatRight').click()
        self.Sleeper()
        email=bot.find_element_by_class_name('js-initial-focus')
        security=bot.find_element_by_class_name('js-password-field')
        email.send_keys(self.username)
        security.send_keys(self.password)
        security.send_keys(Keys.RETURN)
    def Search(self,keyword):
        bot=self.bot
        bot.get('https://twitter.com/search?q='+str(keyword)+'&src=typd')
        self.Sleeper()
        bot.execute_script('window.scroll(0,document.body.scrollHeight)')
        time.sleep(6)
        content=bot.find_elements_by_class_name('has-content')
        links=[]
        for link in content:
            links.append(link.get_attribute('data-permalink-path'))
        print(links)
        return links
    def LikeLinks(self,links):
        bot=self.bot
        for link in links[1:]:

            bot.get('https://www.twitter.com'+str(link))
            try:
                bot.find_element_by_class_name('HeartAnimation').click()
                time.sleep(5)
            except:
                print("Error Occured at "+str(link))
twitter=TwitterBot('ushakeel808',password)
twitter.Login()
twitter.Sleeper()
links=twitter.Search('development')
twitter.LikeLinks(links)
