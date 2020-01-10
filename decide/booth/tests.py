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

class TestConfiguration():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_configuration(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.get("http://127.0.0.1:8000/admin/login/")
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.ID, "id_username").send_keys("admin")
    self.driver.find_element(By.ID, "id_password").send_keys("adminadmin")
    self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".model-voting .addlink").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Test")
    self.driver.find_element(By.ID, "id_desc").click()
    self.driver.find_element(By.ID, "id_desc").send_keys("Test")
    self.driver.find_element(By.CSS_SELECTOR, ".field-question .related-widget-wrapper").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#add_id_question > img").click()
    self.vars["win1356"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to_window(self.vars["win1356"])
    self.driver.find_element(By.ID, "id_desc").send_keys("Test")
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").click()
    self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
    self.driver.find_element(By.ID, "id_options-0-option").click()
    self.driver.find_element(By.ID, "id_options-0-option").send_keys("test1")
    self.driver.find_element(By.ID, "id_options-1-number").click()
    self.driver.find_element(By.ID, "id_options-1-number").send_keys("2")
    self.driver.find_element(By.ID, "id_options-1-option").click()
    self.driver.find_element(By.ID, "id_options-1-option").send_keys("test2")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.switch_to_window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#add_id_auths > img").click()
    self.vars["win8868"] = self.wait_for_window(2000)
    self.driver.switch_to_window(self.vars["win8868"])
    self.driver.find_element(By.ID, "id_name").send_keys("Test")
    self.driver.find_element(By.ID, "id_url").click()
    self.driver.find_element(By.ID, "id_url").click()
    self.driver.find_element(By.ID, "id_url").send_keys("http://127.0.0.1:8000")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.switch_to_window(self.vars["root"])
    element = self.driver.find_element(By.NAME, "_save")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "_save")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "_save")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    #self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.LINK_TEXT, "Inicio").click()
    self.driver.find_element(By.CSS_SELECTOR, ".model-user .addlink").click()
    self.driver.find_element(By.ID, "id_username").send_keys("user1")
    self.driver.find_element(By.ID, "id_password1").click()
    self.driver.find_element(By.ID, "id_password1").send_keys("useruser")
    self.driver.find_element(By.ID, "id_password2").click()
    self.driver.find_element(By.ID, "id_password2").send_keys("useruser")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.LINK_TEXT, "Inicio").click()
    self.wait_for_window(2000)
    self.driver.find_element(By.CSS_SELECTOR, ".model-census .addlink").click()
    self.wait_for_window(2000)
    self.driver.find_element(By.ID, "id_voting_id").send_keys("1")
    self.driver.find_element(By.ID, "id_voter_id").click()
    self.driver.find_element(By.ID, "id_voter_id").send_keys("2")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.LINK_TEXT, "Inicio").click()
    self.driver.find_element(By.LINK_TEXT, "Votings").click()
    self.driver.find_element(By.NAME, "_selected_action").click()
    dropdown = self.driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Start']").click()
    element = self.driver.find_element(By.NAME, "action")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "action")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "action")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "action").click()
    self.driver.find_element(By.NAME, "index").click()
    self.driver.find_element(By.LINK_TEXT, "Inicio").click()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()
