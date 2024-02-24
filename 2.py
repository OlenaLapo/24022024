from selenium import  webdriver
from  selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.maximize_window()

#zaakceptuj zgodę

accept = driver.find_element("id", "L2AGLb")
accept.click()

search = driver.find_element("name", "q")
search.send_keys('Kto ma dzisiaj imieniny')

search.send_keys(Keys.RETURN)
time.sleep(200)
driver.quit()