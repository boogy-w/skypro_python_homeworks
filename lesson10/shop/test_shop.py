import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature('Shopping')
class TestShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.quit()

    @allure.title('Successful Purchase Test')
    @allure.description('Test the full purchase flow from login to checkout.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase(self):
        with allure.step("Login as standard user"):
            login_page = LoginPage(self.driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Add products to the cart"):
            inventory_page = InventoryPage(self.driver)
            inventory_page.add_to_cart_by_product_name("Sauce Labs Backpack")
            inventory_page.add_to_cart_by_product_name("Sauce Labs Bolt T-Shirt")
            inventory_page.add_to_cart_by_product_name("Sauce Labs Onesie")
            inventory_page.go_to_cart()

        with allure.step("Proceed to checkout"):
            cart_page = CartPage(self.driver)
            cart_page.click_checkout()

        with allure.step("Complete checkout information"):
            checkout_page = CheckoutPage(self.driver)
            checkout_page.fill_checkout_info("YourFirstName", "YourLastName", "12345")
            checkout_page.click_continue()

        with allure.step("Verify total amount"):
            total_amount = checkout_page.get_total_amount()
            with allure.step(f"Check if the total amount is $58.29"):
                self.assertEqual(total_amount, 58.29, f"Ожидалось $58.29, но получено ${total_amount:.2f}")

        print("Тест пройден успешно. Общая сумма $58.29")
