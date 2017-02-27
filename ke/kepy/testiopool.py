import requests  
import time  
import gevent.pool  
import gevent.monkey  
  
gevent.monkey.patch_all()  
  

  
def download_requests(url):
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    req = requests.get(url,  
            headers={'user-agent': 'Mozilla/5.0'})  
    #return req.status_code, req.text
  
urls = ['http://www.wsgjp.com.cn/'] * 100
N = 1
PoolNum = 500
  
for i in range(N):  
    print('start %d try' % i)
    #for status, data in jobs:  
    #    print(status, data[:10])  
    #tic(urllibT, 'urllib.request')  


    #jobs = [download_requests(url) for url in urls]
    #for status, data in jobs:  
    #    print(status, data[:10])  
    #tic(requestsT, 'requests')  

    pool = gevent.pool.Pool(PoolNum)  
    data = pool.map(download_requests, urls)  
    #for status, text in data:  
    #    print(status, text[:10])  
    #tic(requestsT, 'requests with gevent.pool')

    print  "gevent...."
    jobs = [gevent.spawn(download_requests, url) for url in urls]  
    gevent.joinall(jobs)  
    #for i in jobs:  
    #    print(i.value[0], i.value[1][:10])  
    #tic(requestsT, 'requests with gevent.spawn')

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