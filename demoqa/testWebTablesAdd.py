from modules import *


# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/elements')
driver.find_element(By.ID, "item-3").click()
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
driver.find_element(By.ID, "firstName").send_keys("Fathima")
driver.find_element(By.ID, "lastName").send_keys("Azzahra")
driver.find_element(By.ID, "userEmail").send_keys("fathimaazzahra0@gmail.com")
driver.find_element(By.ID, "age").send_keys("22")
driver.find_element(By.ID, "salary").send_keys("1000000")
driver.find_element(By.ID, "department").send_keys("Quality Assurance")
driver.find_element(By.ID, "submit").click()

time.sleep(3)
driver.close()