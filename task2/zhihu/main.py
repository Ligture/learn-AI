from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.edge.service import Service
import json
import time
import csv


from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#设置chrome位置
options.binary_location = r"D:\learn-AI\learn-AI\task2\zhihu\chrome\chrome.exe"
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

#设置webdriver服务
service = Service(r"D:\learn-AI\learn-AI\task2\zhihu\chrome\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)
#with open('stealth.min.js', encoding='utf-8') as f: #绕过检测js
    #driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f.read()})
driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
        },
)



#读取cookies
with open("cookies.json",'r',encoding='utf-8') as f:
    cookies = json.loads(f.read())


driver.get("https://www.zhihu.com/topic/20063922/hot")
#driver.get("https://bot.sannysoft.com")

for cookie in cookies:
    driver.add_cookie(cookie)
#访问话题页面
driver.refresh()
time.sleep(1)
# 向下滚动5000个像素 加载更多问题
driver.execute_script('window.scrollBy(0,5000)')
time.sleep(2)
node_list = driver.find_element("xpath",'//*[@id="TopicMain"]/div[4]/div[2]/div/div')
items = node_list.find_elements("xpath",'./div[@class="List-item TopicFeedItem"]/div/div[@class="ContentItem AnswerItem"]')
input()





print(items)