# -*- coding: utf-8 -*-
import multiprocessing
import time
import requests
def func(url):
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('GET: %s' % url)
    '''
    resp = urllib2.urlopen(url)
    data = resp.read()
    '''
    resp = requests.get(url)
    data = resp.text()
    print('%d bytes received from %s.' % (len(data), url))
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    today = datetime.date.today()
    print today


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(4):
        #msg = "hello %d" %(i)
        pool.apply_async(func, ("http://www.wsgjp.com.cn/", ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."