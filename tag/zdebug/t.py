import time
import json
import re
import c
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



a="-s D:/tag/test_module_thread/test_mt_01.py:thread-1,"
casename="test_mt_01"
b=re.findall(""+casename+"(.*?),",a)
print b[0][-1]


