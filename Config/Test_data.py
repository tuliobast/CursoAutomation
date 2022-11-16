from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from 


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver: webdriver.Remote = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    def tearDown(self):
        if self is not None:
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()