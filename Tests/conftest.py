import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome('../chromedriver')
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
