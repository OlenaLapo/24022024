from selenium import webdriver
import time

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"
new_url = "https://www.wp.pl"

# otwarcie okna przeglądarki z konkretnym adresem
driver.get(url)

# wielkość
# konkretna wilkość dobra dla testów
# driver.set_window_size(400, 200)
# maksymalizowanie okna
driver.maximize_window()

# otwarcie nowego okna
driver.execute_script("window.open('');")

# przełączenie się do nowego okna
driver.switch_to.window(driver.window_handles[1])

# uruchomienie nowej strony
driver.get(new_url)

# zamkniecie zakładki
driver.close()

# zatrzymanie skryptu na x sekund
time.sleep(15)

# zakończenie pracy przeglądarki
driver.quit()
#//*[@id="APjFqb"]