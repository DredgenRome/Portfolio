from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('E:/Programs/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://app.destinyitemmanager.com/4611686018468692732/d2/loadouts")
driver.find_element(By.CSS_SELECTOR, "#\\32 6ab59a3-0ba3-4719-943c-7456bb7fc027 .dim-button:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(3) .YZCKKojF:nth-child(1) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529198544139272").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(3) .YZCKKojF:nth-child(2) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529896243095762").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(3) .YZCKKojF:nth-child(3) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529197004483501").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(3) .YZCKKojF:nth-child(4) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529896243094049").click()
driver.find_element(By.CSS_SELECTOR, ".YZCKKojF:nth-child(5) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529896219878261").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(2) .YZCKKojF:nth-child(1) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529197127123329").click()
driver.find_element(By.CSS_SELECTOR, ".cVK6t25b:nth-child(2) .YZCKKojF:nth-child(2) .RxJ3N0KL").click()
driver.find_element(By.ID, "6917529819220899880").click()
driver.find_element(By.CSS_SELECTOR, ".Xg8obMOi").click()
driver.find_element(By.ID, "6917529896230905452").click()
driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(1) > .dim-button").click()
driver.find_element(By.CSS_SELECTOR, "#\\32 6ab59a3-0ba3-4719-943c-7456bb7fc027 .dim-button:nth-child(1)").click()
time.sleep(1)
