# -*- coding: utf-8 -*-
class LoginPage:
    # locators of all the elements
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self, webdriver):
        self.driver = webdriver

    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def loginbutton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
