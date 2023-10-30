import pytest
from selenium import webdriver

# similar to @Before Test
#avoid duplication of webdriver
@pytest.fixture
def setup():
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the Browser value to setup method
    return request.config.getoption("--browser")


###### PyTest HTML Report ########
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Alex'

# it is hook for delete/ Modify enviroment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)


