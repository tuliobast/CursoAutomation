from selenium.webdriver.common.by import By
from Config.Test_data import BaseTest
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote
from selenium import webdriver
import unittest


class Loginpage(BaseTest):

    def __init__(self, driver: Remote):
        super().__init__()
        self.driver = driver

    def input_username(self):
        input = self.driver.find_element(By.ID, 'user-name')
        input.send_keys('standard_user')
        return input

    def input_password(self):
        contrasena = self.driver.find_element(By.ID, 'password')
        contrasena.send_keys('secret_sauce')

    def button_login(self):
        button = self.driver.find_element(By.ID, 'login-button')
        button.click()
        return button

    def do_login(self):
        login_page = Loginpage(self.driver)
        login_page.input_username()
        login_page.input_password()
        login_finish = login_page.button_login()
        return login_finish


