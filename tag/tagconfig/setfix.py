import pytest
import time
import gridnodeset

from common import browserClass

browser=browserClass.browser()

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



@pytest.fixture(scope='session')
def setup_session():
    global flagall
    flagall=[0,1]

@pytest.fixture(scope='function')
def setup_function(request):
    print "driverall len"
    driver=browser.startBrowser(flagall)
    flag=flagall.pop()
    def teardown_function():
        print("teardown_function called.")
        driver.quit()
        flagall.insert(0,flag)
    request.addfinalizer(teardown_function)
    print('setup_function called.')
    browser.set_up(driver)

@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
    request.addfinalizer(teardown_module)
    print('setup_module called.')

@pytest.fixture(scope='class')
def setup_class(request):
    def teardown_class():
        print("teardown_class called.")
    request.addfinalizer(teardown_class)
    print('setup_class called.')
