#*-* coding:UTF-8 *-*
import time
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#res=requests.get("http://www.wsgjp.com.cn/")
#print res.textfrom gevent
import time
import gevent.pool
import gevent.monkey

gevent.monkey.patch_all()
import requests
i=101
def f(url2):
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+('GET: %s' % url2)
    '''
    resp = urllib2.urlopen(url)
    data = resp.read()
    '''

    resp = requests.get(url2)
    global i
    i+=1
    print i
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url2))+" "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #print
'''
gevent.joinall([
        gevent.spawn(f, 'http://www.wsgjp.com.cn/'),
        gevent.spawn(f, 'http://www.wsgjp.com.cn/'),
        gevent.spawn(f, 'http://www.wsgjp.com.cn/'),


])
'''
#urls=["http://www.wsgjp.com.cn/"]*300
urls=["http://dba.wsgjp.com.cn/"]*300
print "pool"
pool = gevent.pool.Pool(300)
data = pool.map(f, urls)



print "no pool"
jobs = [gevent.spawn(f, url) for url in urls]
gevent.joinall(jobs)

print i