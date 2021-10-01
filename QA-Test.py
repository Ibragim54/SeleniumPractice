import time

import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# *****************************************************************************
# Unit test suite
# *****************************************************************************
class AssignTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome()
    cls.driver.maximize_window()
    cls.driver.implicitly_wait(5)
    cls.email = "user@phptravels.com"
    cls.password = "demouser"
    cls.url="http://www.phptravels.net"




  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

  def test1_login_bad_password(self):
    ##########################
    # I - Test bad password login
    ##########################
    self.driver.get("http://www.phptravels.net/login")
    time.sleep(5)
    emailfield = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
    emailfield.clear()
    emailfield.send_keys(self.email)
    passwordfield = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
    passwordfield.clear()
    passwordfield.send_keys("wrongpassword")
    login = self.driver.find_element_by_xpath("//button[text()='Login']")
    login.click()
    time.sleep(5)
    errormessage = self.driver.find_element_by_xpath("//form[@id='loginfrm']/div[@class='panel panel-default']//div[@class='alert alert-danger']")
    errormessagetext = errormessage.text
    self.assertTrue(str(errormessagetext) == "Invalid Email or Password")

  def test2_login(self):
    ##########################
    # I - Test good credentials login
    ##########################
    self.driver.get("http://www.phptravels.net/login")
    time.sleep(5)
    email = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
    email.clear()
    email.send_keys(self.email)
    password = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
    password.clear()
    password.send_keys(self.password)
    login = self.driver.find_element_by_xpath("//button[text()='Login']")
    login.click()
    time.sleep(5)
    self.assertTrue(self.driver.title == 'My Account')

  def search(self, hotel_city, check_in_date, check_out_date, travelers_count):
    ##########################
    # I - Search Method
    ##########################
    self.driver.get("http://www.phptravels.net/login")
    home = self.driver.find_element_by_xpath("//div[@class='container']//a[text()='Home']")
    home.click()
    hotel = self.driver.find_element_by_xpath("//div[contains(@class, 'hotelsearch locationlisthotels')]")
    hotel.click()
    actions = ActionChains(self.driver)
    actions.send_keys(hotel_city).perform()
    result = self.driver.find_element_by_xpath("//div[contains(@class, 'select2-result-label')]//span")
    result.click()
    time.sleep(5)
    check_in = self.driver.find_element_by_xpath("//div[@id='HOTELS']//input[@placeholder='Check in']")
    check_in.clear()
    check_in.send_keys(check_in_date)
    check_out = self.driver.find_element_by_xpath("//div[@id='HOTELS']//input[@placeholder='Check out']")
    check_out.clear()
    check_out.send_keys(check_out_date)
    travelers = self.driver.find_element_by_xpath("//div[@id='HOTELS']//input[@id='travellersInput']")
    travelers.clear()
    travelers.send_keys(travelers_count)
    search = self.driver.find_element_by_xpath("//div[contains(@class,'search-button')]//button")
    search.click()
    time.sleep(5)

  def test3_search_case_1(self):
    ##########################
    # I - Basic Hotel Search
    ##########################
    self.search("Montreal", "15/11/2018", "20/11/2018", "2 Adult 0 Child")
    self.assertTrue(self.driver.title == 'Search Results')

  def test3_search_case_2(self):
    ##########################
    # I - Edge Case Scenario 1
    ##########################
    self.search("Montreal", "20/10/2018", "5/10/2018", "2 Adult 0 Child")
    self.assertTrue(self.driver.title == 'Search Results')

  def test3_search_case_3(self):
    ##########################
    # I - Edge Case Scenario 2
    ##########################
    self.search("Montreal", "15/11/2018", "20/11/2018", "0 Adult 0 Child")
    self.assertTrue(self.driver.title == 'Search Results')

if __name__ == "__main__":
  unittest.main()
