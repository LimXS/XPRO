#*-* coding:UTF-8 *-*
import pytest
#from  tagconfig import setfix
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common import browserClass
import time
browser=browserClass.browser()
'''
c=setfix.setup_function
driver=setfix.driver
browser=setfix.browser
'''

class Testclass():

    def setup_class(cls):
        print ("setup_class----->>")
        #cls.driverlocal=browser.startBrowser('chrome')
        cls.flagall=[0,1]

    def teardown_class(cls):
        print ("teardown_class----->>")

    def setup_method(self,method):
        self.driver=browser.startBrowser(self.flagall)
        self.flag=self.flagall.pop()
        if self.flag==0:
            print "remote......"
        else:
            print "local....."
        print "setup_method........"
        print "flagallpop.............."
        print self.flagall
        browser.set_up(self.driver)

    def teardown(self):
        print "teardown......"
        self.driver.quit()
        self.flagall.insert(0,self.flag)
        print "flagallappend.............."
        print self.flagall


    def test_one(self):
        self.flagall.append(0)
        print('Testmd2_03_11 called.')
        #browser.findId(self.driver,"$1b8bb415$corpName").send_keys("test")
        time.sleep(2)

        #print m+1

    def test_two(self):
        print('Testmd2_03_12 called.')

        #print m+1

    def test_three(self):
        print('Testmd2_03_13 called.')
        time.sleep(1)

    def test_four(self):
        print('Testmd2_03_14 called.')
'''
    def test_five(self):
        print('Testmd2_02_15 called.')


    def test_six(self):
        print('Testmd2_02_16 called.')


class Testclass_md2():
    def test_md1_02_one2(self,c):
        print('Testmd1_02_21 called.')

    def test_md1_02_tow2(self,c):
        print('Testmd1_02_22 called.')

'''

if __name__ == '__main__':
    pytest.main("-d --tx 2*popen --html=../report.html ../test_module1 ")
    #pytest.main("-d --tx 2*popen --html=../report.html test_md1_03.py ")