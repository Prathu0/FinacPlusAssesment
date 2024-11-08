# pages/products_page.py
from selenium.webdriver.common.by import By

class ProductsPage:
    FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")

    def __init__(self, driver):
        self.driver = driver

    def get_first_product_info(self):
        product_name = self.driver.find_element(*self.FIRST_PRODUCT_NAME).text
        product_price = self.driver.find_element(*self.FIRST_PRODUCT_PRICE).text
        return product_name, product_price

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
