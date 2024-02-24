from selenium import webdriver
import time

driver = webdriver.Chrome()

# implicity wait - oczekiwanie na pojawienie sie KAŻDEGO elementu na stronie
driver.implicitly_wait(10)

driver.get("http://www.kurs-selenium.pl/")
driver.maximize_window()

city = driver.find_element("xpath", "//span[text()='Search by Hotel or City Name']")
city.click()
city = driver.find_element("xpath", "//*[@id='select2-drop']/div/input")
city.send_keys("Dubai")
city = driver.find_element("xpath", "//*[@id='select2-drop']/ul/li/ul/li/div")
city.click()

checkin = driver.find_element("name", "checkin")
checkin.send_keys("24/02/2024")

checkout = driver.find_element("name", "checkout")
checkout.send_keys("28/02/2024")

travellers = driver.find_element("name", "travellers")
travellers.click()

adults = driver.find_element("name", "adults")
adults.clear()
adults.send_keys("1")

child = driver.find_element("name", "child")
child.clear()
child.send_keys("2")

search = driver.find_element("xpath", "//*[@id='hotels']/form/div[5]/button")
search.click()

hotels = driver.find_elements("xpath", "//h4[contains(@class, 'list_title')]//b")
hotels_name = [hotel.get_attribute("textContent") for hotel in hotels]

# for hotel in hotels_name:
#     print(hotel)

assert hotels_name[0] == "Jumeirah Beach Hotel"
assert hotels_name[1] == "Oasis Beach Tower"
assert hotels_name[2] == "Rose Rayhaan Rotana"
assert hotels_name[3] == "Hyatt Regency Perth"

time.sleep(10)
driver.quit()