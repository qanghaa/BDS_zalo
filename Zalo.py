from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import random

profile_name=' Profile 10'
options = Options()
options.add_argument("user-data-dir=C:\\Users\\quang\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('profile-directory='+profile_name)
driver = webdriver.Chrome(r"C:\Users\quang\Desktop\BDS_Pj\Chotot\chromedriver.exe", options=options)
# self.driver.get('https://www.bookbub.com/users/sign_in')

def autoLogin(paswd):
    driver.get("https://id.zalo.me/account?continue=https%3A%2F%2Fchat.zalo.me%2F")
# username = WebDriverWait(driver, random.randint(5,10)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input-phone")))
    username = WebDriverWait(driver, random.randint(5,10)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div.zLogin-layout.parentDisable > div.body > div > div > div > div > div.tabs.animated.fadeIn > ul > li:nth-child(2) > a"))).click()
    time.sleep(random.randint(3,10))
    password = WebDriverWait(driver, random.randint(5,10)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div.zLogin-layout.parentDisable > div.body > div > div > div > div > div.content.animated.fadeIn > div:nth-child(1) > div > div > div > div > div.line-form.has-ico > input[type=password]")))
    # username.clear()
    # username.send_keys(email)
    # time.sleep(random.randint(3,10))
    password.clear()
    password.send_keys(paswd)
    time.sleep(random.randint(3,10))
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div.zLogin-layout.parentDisable > div.body > div > div > div > div > div.content.animated.fadeIn > div:nth-child(1) > div > div > div > div > div.textAlign-center.has-2btn > a"))).click()
    time.sleep(random.randint(1,5))


def getDataGroupChat(driver):
    
    # scroll 
    while True:
        # driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        boxChat = driver.find_element_by_id("messageViewScroll")
        time.sleep(1)
        driver.execute_script("return arguments[0].scrollIntoView(true);", boxChat)
        time.sleep(2)
        if random.randint(0, 4) == 3:
            break
    # getdata 
    Result = ""
    time.sleep(random.randint(5,10))
    listMessages = WebDriverWait(driver, random.randint(5,100)).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "chat-item.flx")))
    for Message in listMessages:
        try:
            userName = Message.find_element_by_class_name("card-sender-name").text
            Result += f"{userName}:\n"
            Message_ = Message.find_elements_by_class_name("text")
            for i in Message_:
                Result += f"{i.text}\n"
        except:
            pass
    return Result

    
def getAllData(name,driver):
    clickBoxContacts = WebDriverWait(driver, random.randint(5,10)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__tabs__top > div:nth-child(2)"))).click()
    time.sleep(random.randint(3,10))
    clickBoxGroup = WebDriverWait(driver, random.randint(5,10)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#contactList > div:nth-child(1) > div > div.ReactVirtualized__Grid.ReactVirtualized__List > div > div:nth-child(3)")))
    clickBoxGroup.click()
    time.sleep(random.randint(3,10))
    listGroup = WebDriverWait(driver, random.randint(5,10)).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gr-item")))

    Result = ""
    # get list Group 
    listGroupName = []
    for Group in listGroup: listGroupName.append(Group.find_element_by_class_name("truncate").text)                                                                                                
    
     
    for groupName in listGroupName: #loop groups
        if name in groupName: # check keyword with groupName
            # get data of group 
            for Group in listGroup:
                Group_ = Group.find_element_by_class_name("truncate").text  #name group
                if groupName == Group_:

                    Result += f"Group {groupName}:\n"  
                    Group.click()
                    time.sleep(3)
                    Result += getDataGroupChat(driver)
                    clickBoxGroup.click() # back to list all groups
                    time.sleep(random.randint(3,10))  
                    listGroup = WebDriverWait(driver, random.randint(5,10)).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gr-item")))  #refresh listGroup
                    break
    return Result

driver.get("https://chat.zalo.me")
data = getAllData("Toeic",driver)
print(data)
