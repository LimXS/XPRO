#*-* coding:UTF-8 *-*
import time
from tagconfig import setfix


c=setfix.setup_function
m=setfix.setup_session
browser=setfix.browser

class Testclass_md1():

    def test_one(self,m,c):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('Testmd1_01_11 called.')
        #browser.findId(driver,"$1b8bb415$corpName").send_keys("test")
        time.sleep(3)
        #print m+1

    def test_two(self,c):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('Testmd1_01_12 called.')
        time.sleep(2)
        #print m+1


class Testclass2_md1():
    def test_one2(self,c):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        time.sleep(2)
        print('Testmd1_01_21 called.')


    def test_two2(self,c):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        time.sleep(2)
        print('Testmd1_01_22 called.')



