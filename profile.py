from multiprocessing import set_forkserver_preload
from time import sleep
# from turtle import tilt
# from unicodedata import category
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os ;
class profile():
    def __init__(self,email) -> None:
        options= ChromeOptions()
        cwd = os.getcwd()
        os.chdir(cwd)
        cwd = os.getcwd()
        cwd = "--user-data-dir="+cwd
        options.add_argument(cwd)
        # options.add_argument('--headless')
        options.add_argument('--log-level=3')
        self.mail=email
        self.driver= webdriver.Chrome(options=options)
        self.driver.get("https://outlook.live.com/people/0/")
        sleep(15)
    def find(self):
        el = WebDriverWait(self.driver,timeout=60).until(EC.presence_of_element_located((By.ID,"app")))
        el = WebDriverWait(self.driver,timeout=60).until(EC.presence_of_element_located((By.XPATH,".//div[1]/div[2]/div[2]")))
        el = WebDriverWait(self.driver,timeout=60).until(EC.presence_of_element_located((By.XPATH,".//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/button[1]")))
        el.click()
        sleep(5)
        el = self.driver.find_element(By.ID,"lpc-contact-editor")
        el = el.find_element_by_xpath(".//section[2]/div[2]/div[1]/button[3]/span[1]/span[1]/span[1]")
        el.click()
        el = el.find_element_by_xpath("//div[9]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/button[1]/div[1]/span[1]")
        el.click()
        el = self.driver.find_element(By.ID,"lpc-contact-editor")
        el1 = el.find_element_by_xpath("section[2]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input")
        el1.send_keys(self.mail) 
        el1 = el.find_element_by_xpath(".//section[2]/div[2]/div[1]/button[1]")
        el1.click()
        sleep(10)
        el = self.driver.find_element(By.ID,'app')
        sleep(5)
        el1 = el.find_element_by_xpath(".//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[4]")
        el1.click()
        sleep(5)
        el = self.driver.find_element(By.ID,'app')
        el1 = el.find_element_by_xpath(".//div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[2]/button[1]")
        self.driver.execute_script("console.log(arguments[0]);",el1);
        el1.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        res = self.driver.current_url
        res = res.split('linkedin.com/')
        if res[1].startswith('search'):
           return self.methodTwo()
        else:
            return self.cleanUp(self.driver.current_url)
    def methodTwo(self):
        sleep(10)
        # click on network button on navbar and then continue as written below
        #TODO add click on network button 
        el = self.driver.find_element(By.ID,"global-nav-search")
        el = self.driver.execute_script("""return arguments[0].nextElementSibling""",el)
        el = el.find_element_by_xpath(".//ul[1]/li[2]/a[1]")
        el.click()
        sleep(5)
        el = self.driver.find_element(By.ID,'mynetwork')
        el = el.find_element_by_xpath('div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/a[1]')
        el.click()
        sleep(2)
        # div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]
        el = self.driver.find_element(By.ID,"main")
        el = self.driver.execute_script("""return arguments[0].nextElementSibling""",el)
        el = el.find_element_by_xpath(".//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
        el.click()
        sleep(4)
        el = self.driver.find_element(By.ID,'start-abi')
        el.click()
        sleep(4)
        el = self.driver.find_element(By.ID,"main")
        sleep(4)
        el = el.find_element_by_xpath(".//div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]")
        #/li[1]/div[1]/a[1]
        i =0
        while True:
            i+=1 
            path = ".//li["+str(i)+"]/div[1]/a[1]/div[1]/div[1]/input[1]"
            try : 
                a = el.find_element_by_xpath(path)
                self.driver.execute_script("arguments[0].scrollIntoView();",a)
                # a.click()
                self.driver.execute_script("arguments[0].click();",a)
            except NoSuchElementException: 
                break
        el =self.driver.find_element(By.ID,"main")
        el = el.find_element_by_xpath(".//div[1]/div[1]/div[2]/section[1]/div[1]/ul[1]/li[3]/button[1]")
        el.click()
        sleep(7)
        el = self.driver.find_element(By.ID,"main")
        el = el.find_element_by_xpath(".//div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
        el.click()
        sleep(7)
        el = self.driver.find_element(By.ID,'mynetwork')
        el = el.find_element_by_xpath('div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/a[1]')
        el.click()
        sleep(5)
        self.driver.refresh()
        sleep(7)
        el = self.driver.find_element(By.ID,"main")
        ul = el.find_element_by_xpath("div[1]/div[1]/div[1]/div[1]/ul[1]")
        i=0
        res = []
        while True :
            i+=1
            try :
                li = ".//li["+str(i)+"]/div[1]/div[1]/div[2]/button[1]"
                el = ul.find_element_by_xpath(li)
                el.click()
                sleep(2)
                el = self.driver.find_element(By.ID,"artdeco-modal-outlet")
                el1 = el.find_element_by_xpath(".//div[1]/div[1]/div[3]/div[1]/a[1]").get_attribute("href")
                el1 = "http://www.linkedin.com"+el1
                res.append(el1)
                el = el.find_element_by_xpath(".//div[1]/div[1]/button[1]")
                el.click()
            except NoSuchElementException:
                break
        return self.cleanUp(res)
    def cleanUp(self,res):
        self.driver.switch_to.window(self.driver.window_handles[0])
        # d1/d2/d2/d2/d2/d1/d1/d2/d1/d1/d1/d1/d1 
        app = self.driver.find_element(By.ID,'app')
        # find select all checkbox and then click it 
        btn = app.find_element_by_xpath('div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]')
        btn.click()
        # now find delete button and click it
        btn = app.find_element_by_xpath('div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/button[1]')
        btn.click()
        #now find the delete button in confirmation modal and click it delete the contacts
        btn = self.driver.find_element(By.ID,"lpc__contact_editor_container")
        nxt = self.driver.execute_script("""return arguments[0].nextElementSibling""", btn)
        btn = nxt.find_element_by_xpath("div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]/button[1]")
        btn.click()
        sleep(2)
        self.driver.quit()
        return res
if __name__ == "__main__":
    ob = profile(input("\x1b[6;30;42m email id : \x1b[0m"))
    url = ob.find()
    print('\x1b[6;30;42m'+'link'+'\x1b[0m',end=" : ")
    print(url)
   