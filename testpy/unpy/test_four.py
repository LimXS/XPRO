import unittest
class testforelass(unittest.TestCase):

    def setUp(self):
        print "testthreeclass setup"


    def tearDown(self):
        print "test4class end"
        pass

    def test4_main(self):
        print "444"
        assert 4 != 1