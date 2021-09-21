from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
import json

# 定义一个淘宝类
class TaoBao(object):
    def __init__(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.domain = 'https://passport.jd.com/new/login.aspx'
        self.browser.maximize_window()  # 窗口最大化
        self.browser.implicitly_wait(5)
		
    def  get_cookies(self):
        tb_cookies = self.browser.get_cookies();	
#        print(tb_cookies)

        cookieString = "["
        for cookie in tb_cookies[:-1]:
            cookieString=cookieString+json.dumps(cookie)+','
        cookieString=cookieString+json.dumps(tb_cookies[-1])    
#        print(cookieString+']')
        cookies = json.loads(cookieString+']')
        with open("jd-cookies.json","w") as f:
            print(json.dumps(cookies, sort_keys=True, indent=4),file=f) 		
            f.close()
            
    def open(self):
        self.browser.get(self.domain)
        sleep(1)		
		
		
		
		
		
# main函数入口
if __name__ == "__main__":
    tb = TaoBao()
    tb.open()
    input("login")	
    tb.get_cookies()