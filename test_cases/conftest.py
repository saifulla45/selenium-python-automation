import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser: chrome OR firefox OR edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Please check the browser name")
    return driver


############### for pytest html reports ########################
#hook for adding environment info in html report

def pytest_configure(config):
    config.stash[metadata_key] ["Project Name"] = "Demo Web E-commerce"
    config.stash[metadata_key] ["Test Module"] = "Login"
    config.stash[metadata_key] ["Tester Name"] = "Muhammed Saifulla Attar"

#Hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)

