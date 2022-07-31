import unittest
import HtmlTestRunner
from selenium import webdriver
import time

import sys
sys.path.append("/home/zorro/unittest_project_POMbased")
from page_objects.login_page import LoginPage


class TestLogin(unittest.TestCase):
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Firefox(executable_path="/home/zorro/Downloads/geckodriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()

    def testing_login(self):
        lp = LoginPage(self.driver)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.loginbutton()
        time.sleep(10)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title not the same")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/zorro/unittest_project_POMbased/reports"))
