# pages/cart_page.py
from selenium.webdriver.common.by import By

class CartPage:
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    LOGOUT_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_MENU = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def get_cart_item_name(self):
        return self.driver.find_element(*self.CART_ITEM_NAME).text

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_MENU).click()
