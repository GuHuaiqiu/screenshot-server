from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json
import pymsgbox
import hashlib
from util import fullpage_screenshot
from db import get_db_q

browser_tb=None
browser_jd=None
browser_other=None



class Browser(object):
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("start-maximized")    
        options.add_argument("headless")       
        self.browser = webdriver.Chrome("./chromedriver.exe",chrome_options=options, service_args=['--verbose'])
        self.browser.maximize_window()  # 窗口最大化
        self.browser.implicitly_wait(5)
        
    def clear_cookies(self):
        self.browser.delete_all_cookies()	
        
    def  load_cookies(self,fn):               
        f=open(fn,"r")
        json_cookies=json.load(f)
        f.close()
        for cookie in json_cookies:
           self.browser.add_cookie(cookie) #{"name" : cookie["name"], "value" : cookie["value"]})   

    def open(self,url):
        self.browser.get(url)
		
    def start(self,id,url):
        md5_hash = hashlib.md5()
        md5_hash.update(bytes(id, encoding='ascii'))
        md5_hash.update(bytes(url, encoding='ascii'))        
        md5 = md5_hash.hexdigest()        
        try:
            self.open(url)
            sleep(2)
#            s = self.browser.get_window_size()
#obtain browser height and width
#            w = self.browser.execute_script('return document.body.parentNode.scrollWidth')
#            h = self.browser.execute_script('return document.body.parentNode.scrollHeight')
#            print("w:%d,h:%d"%(w,h))
#            elem = self.browser.find_element_by_tag_name('body')
            # Get the height of the element, and adding some height just to be sage
#            h = elem.size['height'] + 1000
#            w = elem.size['width'] + 1000
#            print("w:%d,h:%d"%(w,h))
#set to new window size
#            self.browser.set_window_size(w, h)
#obtain screenshot of page within body tag
#            self.open(url)
#            sleep(2)
            
            # from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
#            js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
#            h = self.browser.execute_script(js)            
#            self.browser.set_window_size(w, h)
#            self.browser.save_screenshot(md5+'.png')
#            self.browser.find_element_by_tag_name('body').screenshot(md5+'.1.png')                        
#            self.browser.set_window_size(s['width'], s['height'])        
            fullpage_screenshot(self.browser,md5)
            get_db_q().db.add(id,md5,0)
        except Exception as e:
            print(e)
            get_db_q().db.add(id,md5,1)            
            pass
            
    def close(self):
        self.browser.close()    
        
def init_browser():
    global browser_tb,browser_jd,browser_other
    browser_tb=Browser()    
    #browser_tb.open("https://login.taobao.com/member/login.jhtml")
    browser_tb.open("https://www.taobao.com")
    browser_tb.load_cookies("tb-cookies.json")
    browser_jd=Browser()
    #browser_jd.open('https://passport.jd.com/new/login.aspx')
    browser_jd.open("https://www.jd.com")
    browser_jd.load_cookies("jd-cookies.json")
    browser_other=Browser()
    
def deinit_browser():    
    browser_jd.close()
    browser_tb.close()
    browser_other.close()
    
def get_tb():
    return browser_tb    
    
def get_jd():
    return browser_jd        
    
def get_other():
    return browser_other        