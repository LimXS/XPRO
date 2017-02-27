
def a(fun):
    def hehe():
        print "hehe"
        return fun()
    return hehe

def d(fun):
    def hehe():
        print "dddd"
        return fun()
    return hehe
@a
def b():
    global s
    s=100
    print s

@d
def c():
    print "222"
    print b.s
c()


