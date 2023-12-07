import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

year = ['107年', '108年', '109年', '110年', '111年']

class Selenium:

    def __init__(self, driver):
        self.driver = driver

    def get_web(self, url):
        self.driver.get(url)
        time.sleep(1) #等待彈跳視窗出來
        return self.driver

    def click(self, xpath):
        element = self.driver.find_element('xpath', xpath)
        element.click()
        time.sleep(1)
        
    def get_attrib(self, xpath):
        att = self.driver.find_element('xpath', xpath)
        return att

download_path_electronic = r"C:\Users\user\OneDrive - yuntech.edu.tw\文件\Python Scripts\Selenium_the_traffic_web\eletronic_motor" # 下載路徑
download_path_motor = r"C:\Users\user\OneDrive - yuntech.edu.tw\文件\Python Scripts\Selenium_the_traffic_web\motor" # 下載路徑


# 產生一個空的資料夾到指定路徑

import os
if not os.path.exists(download_path_electronic):
    os.makedirs(download_path_electronic)
    print('資料夾建立成功')
else:
    for file in os.listdir(download_path_electronic):
        os.remove(os.path.join(download_path_electronic, file))
    print('資料夾已全部淨空')

if not os.path.exists(download_path_motor):
    os.makedirs(download_path_motor)
    print('資料夾建立成功')

else:
    for file in os.listdir(download_path_motor):
        os.remove(os.path.join(download_path_motor, file))
    print('資料夾已全部淨空')
    




traffic_url = 'https://roadsafety.tw/Dashboard/Custom?type=%E7%B5%B1%E8%A8%88%E5%BF%AB%E8%A6%BD'


# 電動機車

for i in year:
    option_elc = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_path_electronic}
    option_elc.add_experimental_option("prefs", prefs)
    driver_elc = webdriver.Chrome(options = option_elc)
    selenium_elc = Selenium(driver_elc)
    driver = selenium_elc.get_web(traffic_url)
    selenium_elc.click('//*[@id="mdAnnounce"]/div/div/div[1]/button') # 按下close
    selenium_elc.click('//*[@id="header"]/div[1]/div[1]/a[1]') # 按下主題分析

    link = selenium_elc.get_attrib('//*[@id="collapseTopics"]/div/div[2]/div/div[2]/ul/li[4]/a') # 進入電動機車的資料內
    selenium_elc.get_web(link.get_attribute('href')) # 得到連結
    time.sleep(2)

    year_filter = Select(driver.find_element('id', 'ddlCyear'))
    year_filter.select_by_visible_text(i)
    
    place = Select(driver.find_element('id', 'ddlCity'))
    place.select_by_visible_text('全國')
    time.sleep(3)
    selenium_elc.click('//*[@id="ExportSrc"]')
    driver.close()


# 機車

for i in year:
    option_motor = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_path_motor}
    option_motor.add_experimental_option("prefs", prefs)
    driver_motor = webdriver.Chrome(options = option_motor)
    selenium_motor = Selenium(driver_motor)
    driver = selenium_motor.get_web(traffic_url)
    selenium_motor.click('//*[@id="mdAnnounce"]/div/div/div[1]/button') # 按下close
    selenium_motor.click('//*[@id="header"]/div[1]/div[1]/a[1]') # 按下主題分析

    link = selenium_motor.get_attrib('//*[@id="collapseTopics"]/div/div[2]/div/div[2]/ul/li[1]/a') # 進入機車的資料內
    selenium_motor.get_web(link.get_attribute('href')) # 得到連結
    time.sleep(2)

    year_filter = Select(driver.find_element('id', 'ddlCyear'))
    year_filter.select_by_visible_text(i)
    
    place = Select(driver.find_element('id', 'ddlCity'))
    place.select_by_visible_text('全國')
    time.sleep(3)
    
    selenium_motor.click('//*[@id="ExportSrc"]')
    driver.close()



