from modules import *


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('https://demoqa.com/elements')
driver.find_element(By.ID, "item-2").click()
driver.find_element(By.CSS_SELECTOR, "label.custom-control-label").click()

time.sleep(3)
driver.close()