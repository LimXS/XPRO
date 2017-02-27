class Testclass():

    def setup_class(cls):
        print ("setup_module----->>")
        cls.m=100

    def test_one(self):
        print "test_one"
        print self.m
