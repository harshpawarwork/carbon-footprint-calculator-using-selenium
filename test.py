from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Harsh/OneDrive/Desktop/carbon footprint calculator using selenium/carbon.html")

time.sleep(2)

driver.find_element(By.ID, "fuel").send_keys("50")
driver.find_element(By.ID, "electricity").send_keys("40")
driver.find_element(By.ID, "waste").send_keys("10")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(5)

driver.quit()