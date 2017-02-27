import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def test_device1():
    '''
    driver=webdriver.Remote(

        #command_executor="http://administrator:1596321@172.16.0.248.gridlastic.com:80/wd/hub",

        command_executor="http://1596321@172.16.0.248:5555/wd/hub",
        desired_capabilities={
            "browserName":"Chrome"
        }
    )
    '''
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    driver=webdriver.Remote(
        command_executor="http://172.16.0.248:5555/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME

    )

    driver.get("https://www.baidu.com/")
    time.sleep(3)

    #assert 0, device


def test_device2():
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    #time.sleep(1)  # simulate long test time
    time.sleep(3)

    #driver.close()



def test_device3():
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time.sleep(3)
    #time.sleep(1)  # simulate long test time
    '''
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.close()
    print "ok test_device1",device
    '''
    #assert 0