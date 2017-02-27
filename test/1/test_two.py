import unittest

class testtwolass(unittest.TestCase):

    def setUp(self):
        print "testoneclass setup"


    def tearDown(self):
        print "testoneclass"
        pass

    def test2_main(self):
        print "222222"
        assert 5 != 1