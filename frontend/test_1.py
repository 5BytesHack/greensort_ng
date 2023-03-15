from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://213.189.201.229/'
browser = webdriver.Chrome(service=ChromeService(executable_path='chromedriver/chromedriver'))
browser.maximize_window()
browser.implicitly_wait(10)
browser.get(url)
nav_link = browser.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]')
ActionChains(browser).click(nav_link).perform()
nav_link.click()
select = Select(browser.find_element(By.ID, 'exampleFormControlSelect1'))
select.select_by_value("1")
btn = browser.find_element(By.CLASS_NAME, "btn-success")
btn.click()
time.sleep(5)
browser.quit()
