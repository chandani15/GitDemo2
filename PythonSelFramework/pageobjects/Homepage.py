from selenium.webdriver.common.by import By

from pageobjects.Checkoutpage import Checkoutpage


class Homepage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    select = (By.XPATH, "//select[contains(@id, 'Select1')]")

    def __init__(self, driver):
        self.driver = driver

    def click_shop(self):
        self.driver.find_element(*Homepage.shop).click()
        return Checkoutpage(self.driver)

    def fill_name(self):
        return self.driver.find_element(*Homepage.name)

    def fill_email(self):
        return self.driver.find_element(*Homepage.email)

    def fill_pwd(self):
        return self.driver.find_element(*Homepage.pwd)

    def check_checkbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def select_value(self):
        return self.driver.find_element(*Homepage.select)



