import unittest
m=1
class testthreelass(unittest.TestCase):

    def setUp(self):
        print "testthreeclass setup"


    def tearDown(self):
        print "testthreeclass end"
        pass

    def test2_main(self):
        print "333"
        assert 3 != 1