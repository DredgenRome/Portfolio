# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test01SignUP():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_01SignUP(self):
    self.driver.get("https://app.destinyitemmanager.com/login")
    self.driver.find_element(By.LINK_TEXT, "Авторизоваться с помощью Bungie.net").click()
    self.driver.find_element(By.CSS_SELECTOR, ".provider-selector-btn:nth-child(3) .provider-icon").click()
    self.driver.find_element(By.ID, "imageLogin").click()
    self.driver.find_element(By.LINK_TEXT, "Destiny 2").click()
  
