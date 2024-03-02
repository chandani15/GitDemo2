from selenium.webdriver.common.by import By


class Checkoutpage:
    products = (By.XPATH, "//app-card")
    product_name = (By.XPATH, "div//h4/a")
    add_cart = (By.XPATH, "div//button")
    checkout = (By.XPATH, "//a[contains(@class,'btn-primary')]")
    in_cart_products = (By.CSS_SELECTOR, ".media-body")
    in_cart_product_name = (By.CSS_SELECTOR, "h4 a")
    in_cart_success = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def find_products(self):
        return self.driver.find_elements(*Checkoutpage.products)

    def take_product_names(self, element):
        return element.find_element(*Checkoutpage.product_name)

    def click_add_cart(self, element):
        return element.find_element(*Checkoutpage.add_cart)

    def click_checkout(self):
        return self.driver.find_element(*Checkoutpage.checkout)
