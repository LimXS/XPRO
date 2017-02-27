import unittest
class testtwolass(unittest.TestCase):

    def setUp(self):
        print "test2class setup"


    def tearDown(self):
        print "test2class end"
        pass

    def test2_main(self):
        print "222222"
        assert 2 != 1