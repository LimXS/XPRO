#*-* coding:UTF-8 *-*

import zipfile
import time
import datetime
import traceback
import sys
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )
import unittest
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os
import shutil

import smtplib
import mimetypes
import json
from selenium.webdriver.common.action_chains import ActionChains
import requests
class base(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self):

        pass

    '''定位单个元素封装'''
    def findId(self,driver,eid):
        f = driver.find_element_by_id(eid)
        return f