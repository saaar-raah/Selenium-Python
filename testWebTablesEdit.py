import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
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