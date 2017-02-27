#*-* coding:UTF-8 *-*
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from baseClass import base
import time
import re
class browser(base):

    def __init__(self):
        '''
        Constructor
        '''
        #base.__init__(self)

        pass

    #启动浏览器
    '''
    def startBrowser(self,browserType):
        try:
            if browserType.upper()=='CHROME':
                driver=webdriver.Chrome()
            elif browserType.upper()=='IE':
                driver=webdriver.Ie()
            elif browserType.upper()=='FIREFOX' or browserType.upper()=='FF':
                driver=webdriver.Firefox()
            else:
                driver=u"无此浏览器类型"
            return driver
        except:
            print(u'启动浏览器失败')
    '''
    def startBrowser(self,flagall):
        while len(flagall)==0:
            continue
        else:
            print "flagall.............."
            print flagall

            if flagall[-1]==1:
                self.driver=webdriver.Firefox()
            else:
                self.driver=webdriver.Remote(
                command_executor="http://172.16.0.248:5555/wd/hub",
                desired_capabilities=DesiredCapabilities.CHROME
            )
            '''
            if len(flagall)==1:
                if flagall[-1]==0:
                    self.driver=webdriver.Firefox()
                else:
                    self.driver=webdriver.Remote(
                    command_executor="http://172.16.0.248:5555/wd/hub",
                    desired_capabilities=DesiredCapabilities.CHROME
                )
            '''
            return self.driver

    def startBrowser2xml(self,flag):
        if str(flag)=='1':
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Remote(
            command_executor="http://172.16.0.248:5555/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
            )
        return driver


    def set_up(self,driver):

        url="https://www.baidu.com/"
        #time.sleep(1)
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(15)

    def writeflags(self,flags):
        ff=open(r"D:\tag\tagconfig\flag",'w')
        ff.write('')
        kk=open(r"D:\tag\tagconfig\flag",'w+')
        n=0
        for a in flags:
            kk.write(a)
            if n<len(flags)-1:
                kk.write(',')
                n+=1
        kk.close()

    def nowstate(self,casename):
        flaguse=''
        while len(flaguse)==0:
            f=open(r"D:\tag\tagconfig\flag",'r')
            flag=f.read()
            f.close()
            flaguse=re.findall(""+casename+"(.*?),",flag)
            continue
        else:
            print flaguse
            use=str(flaguse[0][-1])
        return use
