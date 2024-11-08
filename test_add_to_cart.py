import unittest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.base_test import BaseTest

class TestAddToCart(BaseTest):

    def test_login_and_add_to_cart(self):
        # Step 1: Navigate to Saucedemo.com
        self.driver.get("https://www.saucedemo.com/")
        
        # Step 2: Log in with valid credentials
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Step 3: Verify we are on the products page
        products_page = ProductsPage(self.driver)
        self.assertTrue(products_page.is_product_page(), "Not on the Products Page")
        
        # Step 4: Get the first product name and price and store them in a text file
        first_product = products_page.get_first_product_info()
        with open('resources/product_info.txt', 'w') as file:
            file.write(f"Product: {first_product['name']}\n")
            file.write(f"Price: {first_product['price']}\n")
        
        # Step 5: Add the product to the cart
        products_page.add_first_product_to_cart()
        
        # Step 6: Navigate to the cart page and verify the product is there
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        cart_page.verify_product_in_cart(first_product['name'])
        
        # Step 7: Log out
        products_page.logout()

if __name__ == "__main__":
    unittest.main()
