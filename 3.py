from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# implicity wait - oczekiwanie na pojawienie sie KAŻDEGO elementu na stronie
# driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# zaakceptuj ciasteczka
accept = driver.find_element("id", "accept-choices")
accept.click()

# wybranie menu "Tutorials"
menu = driver.find_element("id", "navbtn_tutorials")
# klikanie w element
# menu.click()
# klikanie w element za pomocom akcji
webdriver.ActionChains(driver).move_to_element(menu).perform()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# wybranie tutoriala "HTML"
# skopiowaney xpath
#tutorial = driver.find_element("xpath", "//*[@id='tutorials_html_css_links_list']/div[1]/a[1]")
# xpath napisany manualnie
tutorial = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
tutorial.click()

# explicit wait
# oczekiwanie na konktetnie ten jeden element przez 10 sekun z czestotliwoscia 0.5 sekundy
wait = WebDriverWait(driver, 10, 0.5)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='leftmenuinnerinner']/a[43]")))

wait.until(lambda x: len(x.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")))
# wybór z lewego menu "Input types"
inputTypes = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")
inputTypes.click()

time.sleep(200)
driver.quit()