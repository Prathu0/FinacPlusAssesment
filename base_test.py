# utils/base_test.py
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Or any WebDriver you are using
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
