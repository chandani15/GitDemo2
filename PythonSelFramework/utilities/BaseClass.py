import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_presence_byclassname(self, text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, text)))

    def select_option_by_visible_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        testCaseName = inspect.stack()[1][3]
        logger = logging.getLogger(testCaseName)
        #logger = logging.getLogger(__name__)
        filename = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filename.setFormatter(formatter)
        logger.addHandler(filename)

        logger.setLevel(logging.INFO)

        return logger