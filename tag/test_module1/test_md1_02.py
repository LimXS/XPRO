#*-* coding:UTF-8 *-*
import pytest
#from  tagconfig import setfix
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common import browserClass
import time
browser=browserClass.browser()


class Testclass():

    def setup_class(cls):
        print ("setup_class----->>")
        #cls.driverlocal=browser.startBrowser('chrome')
        cls.driverall=[]
        cls.flagall=[0,1]

    def setup_method(self,method):
        print ("setup_method----->>")
        while len(self.flagall)==0:
            continue
        else:
            print "flagall.............."
            print self.flagall
            if self.flagall[-1]==0:
                self.driver=webdriver.Firefox()
            else:
                self.driver=webdriver.Remote(
                command_executor="http://172.16.0.248:5555/wd/hub",
                desired_capabilities=DesiredCapabilities.CHROME
            )

            self.flag=self.flagall.pop()
            if self.flag==0:
                print "remote......"
            else:
                print "local....."
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
        print('Testmd1_02_11 called.')
        #browser.findId(self.driver,"$1b8bb415$corpName").send_keys("test")
        time.sleep(2)

        #print m+1

    def test_two(self):
        print('Testmd1_02_12 called.')

        #print m+1

    def test_three(self):
        print('Testmd1_02_13 called.')
        time.sleep(1)

    def test_four(self):
        print('Testmd1_02_14 called.')
'''
    def test_five(self):
        print('Testmd1_02_15 called.')

    def test_six(self):
        print('Testmd1_02_16 called.')


class Testclass_md2():
    def test_md1_02_one2(self,c):
        print('Testmd1_02_21 called.')

    def test_md1_02_tow2(self,c):
        print('Testmd1_02_22 called.')

'''

if __name__ == '__main__':
    pytest.main(" --collect-only ./test_md1_02.py -s ")
    print "start"
    pytest.main(" ./test_md1_02.py::Testclass::test_one -s ")
    #pytest.main("-d --tx 2*popen --html=../report.html test_md1_03.py test_md1_02.py ")
    #pytest.main("  --junitxml=./log3.xml D:/Python27/Scripts/test/1/test_one.py ")