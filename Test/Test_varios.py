from selenium.webdriver.common.by import By
from Config.Test_data import BaseTest
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote
from selenium import webdriver
import unittest
from Pages.Login_page import Loginpage
from Pages.Varios_page import Elements_Varios
import time


class VariosCase(BaseTest):

    def test_filter_lohi(self):
        filter_test = Loginpage(self.driver)
        filter_lohi_test = Elements_Varios(self.driver)
        filter_test.do_login()
        time.sleep(2)
        filter_lohi_test.drop_down_lohi_filters()
        time.sleep(2)
