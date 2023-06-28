from selenium import webdriver
from selenium.webdriver.common.by import By


class Test01Smoke():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_01Smoke(self):
    self.driver.get("https://app.destinyitemmanager.com/login")
    self.driver.find_element(By.LINK_TEXT, "Авторизоваться с помощью Bungie.net").click()
  
