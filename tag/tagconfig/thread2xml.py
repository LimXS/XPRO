# -*- coding: utf-8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
多线程并发，一台电脑一个线程一个driver，可以按模块分配case，也可以按文件分配case，几个线程就生成几个html，最后进行合并

#方法1
#遍历测试的case，并生成url 几个线程就生成几个url 轮流 加入 [test_md1_01.py,test_md1_02.py,test_md1_03.py.................],os+正则
#如果三台电脑，location/3余数0第一台电脑，locationlen(List)/3 余数1第2台电脑，以此内推 flag 为 0,1,2 写入文件，用字典形式写入 如abc{test_md1_01.py:0,test_md1_01.py:1...}
#case写法 在定义driver时候 读取文件并转json 根据字典键值分配driver,如果是三台电脑 则使用三种driver，三个线程
#执行case ，url=-d  --html=../report.html test_xx_xx.py test_xx_xx.py ........
#合并html

#方法2
#遍历所有cases 每次从列表取出case 放入线程 每个case生成一个xml 最后用jenkins生成xml测试报告
'''
import pytest
import time
import Queue
import threading
import beaftest
beaf=beaftest.beaftestClass()

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

#传入的是任务执行命令 获取空余线程名字 用于分配任务
def download_file(url ):
    lock.acquire()
    print threading.currentThread().getName()
    print "case...."
    print url

    thname=str(threading.currentThread().getName())
    #name=str(threading.currentThread().getName())
    #任务使用的线程写入flag文件，便于提取
    f=open(r"D:\tag\tagconfig\flag",'a')
    f.write(url+":")
    f.write(str(thname)+",")
    f.close()
    lock.release()
    #执行测试用例
    pytest.main(url)

def download_file2(url) :
    pytest.main(url)


def main():
    num_of_threads = 2
    #获取case
    caselists=beaf.caseswalk(r"D:\tag\test_module_thread")
    #拼接成命令
    urls=beaf.getcommands2(caselists)
    f=open(r"D:\tag\tagconfig\flag",'w')
    f.write("")
    f.close()
    _st = time.time()
    wm = workerManger(num_of_threads)
    #print num_of_threads
    #urls = ['-d --tx 2*popen --html=../report2.html ../test_module1','-d --tx 2*popen --html=../report.html ../test_module2']
    for i in urls:
        wm.add_job(download_file, i  )
    wm.start()
    wm.wait_for_complete()
    print time.time() - _st




if __name__ == '__main__':
  main()




