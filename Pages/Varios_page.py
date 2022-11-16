from selenium.webdriver.common.by import By
from Config.Test_data import BaseTest
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Elements_Varios(BaseTest):

    def __init__(self, driver: Remote):
        super().__init__()
        self.driver = driver

    def drop_down_lohi_filters(self):
        drop = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        drop.send_keys('p', Keys.ENTER)

    def price_item(self):
        return self.driver.find_element(By.CLASS_NAME, 'inventory_item_price')

