# -*- coding: utf-8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
import requests
import time
import Queue
import threading
lock=threading.Lock()
class Worker(threading.Thread):
    def __init__(self,tagQueue,resultQueue,**kwds):
        threading.Thread.__init__(self,**kwds)
        self.tagQueue=tagQueue
        self.resultQueue = resultQueue


    def run(self):
        while 1:
            try:
                callable,args,kws=self.tagQueue.get(False)
                res=callable(*args,**kws)
                self.resultQueue.put(res)  # put result
            except Queue.Empty:
                break

class workerManger:
    def __init__(self,num_workers=10):
        self.tagQueue=Queue.Queue()
        self.resultQueue = Queue.Queue()  # 输出结果的队列
        self.workers=[]
        self._recruitThreads(num_workers)

    def _recruitThreads(self, num_workers):
        for i in range(num_workers):
            worker = Worker(self.tagQueue, self.resultQueue)  # 创建工作线程
            self.workers.append(worker)  # 加入到线程队列

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()  # 从池中取出一个线程处理请求
            worker.join()
            if worker.isAlive() and not self.tagQueue.empty():
               self.workers.append(worker)  # 重新加入线程池中
        print 'All jobs were complete.'


    def add_job(self, callable, *args, **kwds):
         self.tagQueue.put((callable, args, kwds))  # 向工作队列中加入请求

    def get_result(self, *args, **kwds):
        return self.resultQueue.get(*args, **kwds)

#生成url
def createorderdata(n):
    a=["a"]
    senddata=a*n
    '''
    today = datetime.date.today()
    today=today.strftime('%Y-%m-%d')
    for k in range(n):
        nskdata=(
        {"bill":{"date":"2016-12-27","draft":False,"displaynumber":"","number":"TEST2-JHD20161227-"+rannum[:-6]+str(k),"inputno":"2605638079543105363",
                 "inputfullname":"xsx","redword":False,"redold":False,"billtype":0,"ktypeid":"2605638079543104740","kfullname":"主仓库",
                 "btypetax":0,"todate":today,"efullname":"001","currencyid":0,"btypeid":"2605638088187950285",
                 "bfullname":"t5123443","etypeid":"2605638088210451192","summary":"222222222222","comment":"222222222222",
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"",
                         "pic_url":"http://wd.geilicdn.com/vshop520219391-1459218328272-4913776.png?w=480&h=0","ptypeid":"869585272784951",
                         "pfullname":"002 无编码修改_Ax","pname":"002","ptypecode":"a1x","brandname":"","temp_ucode":"a1x","temp_ucode_flag":True,
                         "ptypeunit":"个","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"","ptypearea":"","snenabled":0,"ptypeweight":0,
                         "oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,"pstatus":0,"comment":"",
                         "prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":29.5,"ptypeweightall":0,
                         "tax":0,"showstockqty":230,"assdpprice":13.6,"discount":1,"assqty":1,"price":13.6,"dpprice":13.6,"qty":1,"dptotal":13.6,
                         "asstpprice":13.6,"tpprice":13.6,"tptotal":13.6,"taxtotal":0,"assprice":13.6,"total":13.6,"mallfee":0,"urate0":"","urate1":"",
                         "urate2":""}],"isover":False,"../Selector/BTypeSelector.gspx":"00003","customerreceiver":None,"customerreceivermobile":None,
             "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
             "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","total":13.6,"ftypeid":0}}
        )
        senddata.append(nskdata)
    '''
    return senddata

def sendandcompare(senddata,headers):
    url2="http://www.wsgjp.com.cn/"
    print threading.current_thread().name+":"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #print threading.current_thread().name
    print('GET: %s' % url2)
    res=requests.get("http://www.wsgjp.com.cn/")
    #print res.text
    print('%d bytes received from %s.' % (len(res.text), url2))
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


def main():

    a=[2000]
    for num in a:


        senddata=createorderdata(2000)
        #n=0
        print len(senddata)
        num_of_threads = num
        _st = time.time()
        wm = workerManger(num_of_threads)
        print num_of_threads
        headers=1

        for i in senddata:
            try:
                wm.add_job(sendandcompare,i,headers)
            except:
                pass
        #wm.get_result(printer,resault_list)
        wm.start()
        wm.wait_for_complete()

        usetime=time.time() - _st
        print usetime
        print 'result Queue\'s length == %d '% wm.resultQueue.qsize()
        '''
        while wm.resultQueue.qsize():
            a=wm.resultQueue.get()
            for i in a :
                print i
        '''

        print usetime

if __name__ == '__main__':
  main()



