import urllib.request  
import requests  
import time  
import gevent.pool  
import gevent.monkey  
  
gevent.monkey.patch_all()  
  
def startTimer():  
    return time.time()  
  
def ticT(startTime):  
    useTime = time.time() - startTime  
    return round(useTime, 3)  
  
#def tic(startTime, name):  
#    useTime = time.time() - startTime  
#    print('[%s] use time: %1.3f' % (name, useTime))  
  
def download_urllib(url):  
    req = urllib.request.Request(url,  
            headers={'user-agent': 'Mozilla/5.0'})  
    res = urllib.request.urlopen(req)  
    data = res.read()  
    try:  
        data = data.decode('gbk')  
    except UnicodeDecodeError:  
        data = data.decode('utf8', 'ignore')  
    return res.status, data  
  
def download_requests(url):  
    req = requests.get(url,  
            headers={'user-agent': 'Mozilla/5.0'})  
    return req.status_code, req.text  
  
urls = ['http://www.ustchacker.com'] * 10  
urllibL = []  
requestsL = []  
reqPool = []  
reqSpawn = []  
N = 20  
PoolNum = 100  
  
for i in range(N):  
    print('start %d try' % i)  
    urllibT = startTimer()  
    jobs = [download_urllib(url) for url in urls]  
    #for status, data in jobs:  
    #    print(status, data[:10])  
    #tic(urllibT, 'urllib.request')  
    urllibL.append(ticT(urllibT))  
    print('1')  
      
    requestsT = startTimer()  
    jobs = [download_requests(url) for url in urls]  
    #for status, data in jobs:  
    #    print(status, data[:10])  
    #tic(requestsT, 'requests')  
    requestsL.append(ticT(requestsT))  
    print('2')  
      
    requestsT = startTimer()  
    pool = gevent.pool.Pool(PoolNum)  
    data = pool.map(download_requests, urls)  
    #for status, text in data:  
    #    print(status, text[:10])  
    #tic(requestsT, 'requests with gevent.pool')  
    reqPool.append(ticT(requestsT))  
    print('3')  
      
    requestsT = startTimer()  
    jobs = [gevent.spawn(download_requests, url) for url in urls]  
    gevent.joinall(jobs)  
    #for i in jobs:  
    #    print(i.value[0], i.value[1][:10])  
    #tic(requestsT, 'requests with gevent.spawn')  
    reqSpawn.append(ticT(requestsT))  
    print('4')  
'''
import matplotlib.pyplot as plt  
x = list(range(1, N+1))  
plt.plot(x, urllibL, label='urllib')  
plt.plot(x, requestsL, label='requests')  
plt.plot(x, reqPool, label='requests geventPool')  
plt.plot(x, reqSpawn, label='requests Spawn')  
plt.xlabel('test number')  
plt.ylabel('time(s)')  
plt.legend()  
plt.show()
'''