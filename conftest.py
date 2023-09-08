from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--start-maximized")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--start-maximized")


@pytest.fixture(scope='class', autouse=True)
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'Chrome':
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Edge(options=edge_options)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait
    #yield
    #driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default='Chrome')


