import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common import browserClass

browser=browserClass.browser()
driverlocal=browser.startBrowser('chrome')

driverall=[]
nodelists=["http://172.16.0.248:5555/wd/hub"]
for a in nodelists:
    nodedriver=webdriver.Remote(
        command_executor=a,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driverall.append(nodedriver)
driverall.append(driverlocal)
innot="driver"