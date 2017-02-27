#*-* coding:UTF-8 *-*
import unittest
class testoneclass(unittest.TestCase):
    u'''测试类1'''

    def setUp(self):
        print "testoneclass setup"


    def tearDown(self):
        print "testoneclass"
        pass

    def test_one(self):
        u'''测试方法1'''
        print "1111"
        try:
            assert 5 != 5
        except:
            print "unequal"
