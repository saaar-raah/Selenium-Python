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
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").click()
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").click()
driver.find_element(By.ID, "postal-code").send_keys("723453")
driver.execute_script("window.scrollTo(0, 80)")
time.sleep(0.5)

driver.find_element(By.ID, "continue").click()
driver.execute_script("window.scrollTo(0,300)")
time.sleep(0.5)
driver.find_element(By.ID, "finish").click()
driver.find_element(By.ID, "back-to-products").click()

time.sleep(2)
driver.close()
