#*-* coding:UTF-8 *-*
import shutil
import time
import os
import re
import math
class beaftestClass():
    #删除文件夹并重新创建
    def deleteandmkdir(self):
        shutil.rmtree(r"D:\screentestpic")
        #print "delete"
        time.sleep(1)
        os.mkdir(r"D:\screentestpic")

    #遍历case
    def caseswalk(self,rootDir):
        caselists=[]
        for root, dirs, files in os.walk(rootDir):
            for file in files:
                #print type(file)
                if len(re.findall("test_(.*?)\.py$",file))!=0:
                    #print(os.path.join(root, file))
                    caselists.append(os.path.join(root, file))

        return caselists

    #等分list
    def cutlist(self,s,n):
        '''
        fn = len(s)/n
        rn = len(s)%n
        ar = [fn+1]*rn+ [fn]*(n-rn)
        si = [i*(fn+1) if i<rn else (rn*(fn+1)+(i-rn)*fn) for i in xrange(n)]
        sr = [s[si[i]:si[i]+ar[i]] for i in xrange(n)]
        return sr
        '''
        fn = len(s)/n
        rn = len(s)%n
        sr = []
        ix = 0
        for i in xrange(n):
            if i<rn:
                sr.append(s[ix:ix+fn+1])
                ix += fn+1
            else:
                sr.append(s[ix:ix+fn])
                ix += fn
        return sr

    def getcommands(self,arr):
        casesurl=[]
        for caselists in arr:
            caseurl="-d --html=../report.html"
            for case in caselists:
                recase=case.replace('\\','/')
                caseurl=caseurl+" "+recase
            casesurl.append(caseurl)
        return casesurl

    def getcommands2(self,arr):
        casesurl=[]
        for case in arr:
            recase=case.replace('\\','/')
            #print recase
            casename=re.findall(":(.*?).py$",recase.replace('/','_'))
            #print casename
            #caseurl="--junitxml=../reports_result/"+casename[0]+".xml "+recase
            caseurl="-s "+recase
            casesurl.append(caseurl)

        return casesurl




'''
a=beaftestClass()
m=a.caseswalk(r"D:\tag\test_module_thread")
print m
#arr=a.cutlist(m,2)
casesurl=a.getcommands2(m)
for a in casesurl:
    print a
'''