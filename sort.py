from modules import *



driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
 
driver.find_element(By.ID, "user-name").click()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.CSS_SELECTOR, "select.product_sort_container").click()
driver.find_element(By.XPATH,"//option[@value='lohi']").click() 

time.sleep(2)
driver.close()
