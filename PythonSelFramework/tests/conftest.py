import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="select browser"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    elif browser == "Edge":
        service_obj = Service()
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    # return driver
    request.cls.driver = driver  # when there is yield we cannot return anything, so we are assigning the
    # local driver to request.cls.driver. So whichever class uses this fixture
    # will have a class variable driver. Hence, we will use as self.driver in that class methods.
    yield
    driver.close()


