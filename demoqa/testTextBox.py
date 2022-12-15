from modules import *


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://demoqa.com/elements')
driver.find_element(By.ID, "item-0").click()
driver.find_element(By.ID, "item-0").click()
driver.find_element(By.ID, "userName").click()
driver.find_element(By.ID, "userName").send_keys("Fathima Azzahra")
driver.find_element(By.ID, "userEmail").send_keys("fathimaazzahra0@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Balikpapan")
driver.find_element(By.ID, "permanentAddress").send_keys("Balikpapan")
driver.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(3)
driver.close()