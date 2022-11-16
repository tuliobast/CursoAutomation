from selenium.webdriver.common.by import By
from Config.Test_data import BaseTest
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote
from selenium import webdriver
from Pages.Login_page import Loginpage
import unittest
import time


class Login(BaseTest):

    def test_login_ok(self):
        self.login_exitoso = Loginpage(self.driver)
        self.login_exitoso.input_username()
        self.login_exitoso.input_password()
        time.sleep(5)
        self.login_exitoso.button_login()

