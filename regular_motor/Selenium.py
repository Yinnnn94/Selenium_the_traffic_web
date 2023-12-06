import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

year = ['107年', '108年', '109年', '110年', '111年']
def get_web(url, opt):
    driver = webdriver.Chrome(options = opt)
    driver.get(url)
    time.sleep(1) #等待彈跳視窗出來
    return driver

def click(driver, xpath):
    element = driver.find_element('xpath', xpath)
    element.click()
    time.sleep(1)
    
def get_attrib(driver, xpath):
    att = driver.find_element('xpath', xpath)
    return att

download_path_electronic = r'C:\Users\user\OneDrive - yuntech.edu.tw\文件\Python Scripts\Big_data\電動機車'

for i in year:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_path_electronic}
    chrome_options.add_experimental_option("prefs", prefs)

    traffic_url = 'https://roadsafety.tw/Dashboard/Custom?type=%E7%B5%B1%E8%A8%88%E5%BF%AB%E8%A6%BD'

    driver = get_web(traffic_url, chrome_options)
    click(driver, '//*[@id="mdAnnounce"]/div/div/div[1]/button') # 按下close
    click(driver, '//*[@id="header"]/div[1]/div[1]/a[1]') # 按下主題分析
    link = get_attrib(driver, '//*[@id="collapseTopics"]/div/div[2]/div/div[2]/ul/li[4]/a') # 進入電動機車的資料內

    driver.get(link.get_attribute('href')) # 得到連結
    time.sleep(3)

    year = Select(driver.find_element('id', 'ddlCyear'))
    year.select_by_visible_text(i)
    place = Select(driver.find_element('id', 'ddlCity'))
    place.select_by_visible_text('全國')
    time.sleep(3)
    click(driver, '//*[@id="ExportSrc"]')
    driver.close()
           



