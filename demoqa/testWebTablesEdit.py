from modules import *


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/webtables')
driver.find_element(By.CSS_SELECTOR, "#edit-record-1 > svg").click()
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "firstName").send_keys("new")
driver.find_element(By.ID, "lastName").click()
driver.find_element(By.ID, "lastName").send_keys("new")
driver.find_element(By.ID, "userEmail").click()
driver.find_element(By.ID, "userEmail").send_keys("")
driver.find_element(By.ID, "age").click()
driver.find_element(By.ID, "age").send_keys("1")
driver.find_element(By.ID, "salary").click()
driver.find_element(By.ID, "salary").send_keys("5000")
driver.find_element(By.ID, "department").click()
driver.find_element(By.ID, "department").send_keys("Auditor")
driver.find_element(By.ID, "submit").click()

time.sleep(3)
driver.close()