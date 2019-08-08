from selenium import webdriver
import os
import time
import configparser
from selenium.webdriver.common.keys import Keys

class InstagramBot:
    
    def __init__(self, username, password):
        """
        Args:
            username:str: username for instagram
            password:str: password for instagram
            
        Attribute: 
            driver:selenium.webdriver.Chrome: The Chrome driver that is used to automate browser action
        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
        '''
        For Incognito mode
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        
        For Internet Explorer
            self.driver =  webdriver.Ie("IEDriverServer.exe")
        '''
        self.login()
        
    def searchUser(self, user):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
        time.sleep(2)
        search_list = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
        search_list.click()
          
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))  
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys(self.password) 
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        time.sleep(3)
        NotNow = self.driver.find_elements_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        time.sleep(2)  
        NotNow[0].click()
        time.sleep(2)    
        
    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))
        
    def follow_user(self, user):
        self.nav_user(user)     
        follow_button_list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")        
        follow_button_list[0].click()
        
    def unfollow_user(self, user):
        self.nav_user(user)
        un_follow_button_list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")   
        un_follow_button_list[0].click()
        un_follow_list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")   
        un_follow_list[0].click()
        
    '''def likeLatestPosts(self, user, n_posts, like=True):
        action = 'Like' if like else 'Unlike'
        self.nav_user(user)
        imgs = []
        imgs.extend(self.driver.find_element_by_class_name("_9AhH0"))
        for img in imgs[:n_posts]:
            time.sleep(1)
            img.click() 
            time.sleep(2) 
            try:
                time.sleep(1)
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click()
                time.sleep(2)
                #self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/a").click()
            except Exception as e:
                print(e)
            #self.comment_post('beep boop testing bot')
            #self.driver.find_elements_by_class_name('ckWGn')[0].click()

    def comment_post(self, text):
        #"""
        #Comments on a post that is in modal form
        #"""
        label = 'Add a comment…'
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(label)).send_keys(text)'''
        
       

        
if __name__ == "__main__":
       
    config = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config)
    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']
    bot = InstagramBot(username, password)
    time.sleep(2)
    
    #bot.likeLatestPosts('arianagrande', 2, like=True)

    
    
    