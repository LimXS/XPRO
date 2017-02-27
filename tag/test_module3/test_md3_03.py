#*-* coding:UTF-8 *-*
from  tagconfig import setfix


c=setfix.setup_function
driver=setfix.driver
browser=setfix.browser

class Testclass():

    def test_one(self,c):
        print('Testmd3_03_11 called.')
        browser.findId(driver,"$1b8bb415$corpName").send_keys("test")
        #print m+1

    def test_two(self):
        print('Testmd3_03_12 called.')
        #print m+1


class Testclass2():
    def test_one2(self):
        print('Testmd3_03_21 called.')

    def test_two2(self):
        print('Testmd3_03_22 called.')