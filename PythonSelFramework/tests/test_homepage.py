import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.Homepage import Homepage
from testdata.TestData import TestDataHomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self, getData):
        homepage = Homepage(self.driver)
        #homepage.fill_name().send_keys("Chandani")
        homepage.fill_name().send_keys(getData["name"])
        homepage.fill_email().send_keys(getData["email"])
        homepage.fill_pwd().send_keys(getData["pwd"])
        homepage.check_checkbox().click()

        self.select_option_by_visible_text(homepage.select_value(), "Female")
        #dropdown = Select(homepage.select_value())
        #dropdown.select_by_visible_text("Female")

        self.driver.find_element(By.ID, "inlineRadio2").click()
        self.driver.find_element(By.NAME, "bday").send_keys("1989-10-10")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        message = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
        print(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=TestDataHomePage.getTestData("TC2"))
    def getData(self, request):
        return request.param