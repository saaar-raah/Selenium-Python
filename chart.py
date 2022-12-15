from modules import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
 
driver.find_element(By.ID, "user-name").click()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

time.sleep(2)
driver.close()
