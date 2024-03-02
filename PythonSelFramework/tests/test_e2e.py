import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from pageobjects.Homepage import Homepage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        products = ["Samsung Note 8", "Nokia Edge"]

        logger = self.getLogger()
        logger.info("Starting the test e2e")

        homepage = Homepage(self.driver)
        checkoutpage = homepage.click_shop()
        #homepage.click_shop().click()
        #self.driver.find_element(By.LINK_TEXT, "Shop").click()

        #checkoutpage = Checkoutpage(self.driver)
        elements = checkoutpage.find_products()
        #elements = self.driver.find_elements(By.XPATH, "//app-card")

        for element in elements:
            name = checkoutpage.take_product_names(element).text
            #name = element.find_element(By.XPATH, "div//h4/a").text
            if name in products:
                logger.info("product name found: "+name)
                checkoutpage.click_add_cart(element).click()
                #element.find_element(By.XPATH, "div//button").click()

        checkoutpage.click_checkout().click()
        #self.driver.find_element(By.XPATH, "//a[contains(.,'Checkout')]").click()

        cart = []
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".media-body")
        for ele in elements:
            cart.append(ele.find_element(By.CSS_SELECTOR, "h4 a").text)

        assert cart == products


        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("In")

        self.verify_presence_byclassname("suggestions")
        #wait = WebDriverWait(self.driver, 15)
        #wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "suggestions")))

        countries = self.driver.find_elements(By.CSS_SELECTOR, "div[class=suggestions] ul")
        for country in countries:
            country_name = country.find_element(By.XPATH, "li/a").text
            print(country_name)
            if country_name == "India":
                country.find_element(By.XPATH, "li/a").click()
                break

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        message = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
        logger.info(message)
        assert "Success!" in message

