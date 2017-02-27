import pytest
@pytest.fixture(scope='session')
def setup_session(request):
    def teardown_session():
        print("teardown_session called.")
    request.addfinalizer(teardown_session)
    print('setup_session called.')
    m=1000
    #print m
    print m
    return m

@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_functions called.")
    request.addfinalizer(teardown_function)
    print('setup_function called.')
    #x=a()
    #print x
    #m+=1
    #print m
class Testclass():
    def test_four(self,setup_session,setup_function):
        print('Test_4 called.')

    def test_five(self):
        print('Test_5 called.')


