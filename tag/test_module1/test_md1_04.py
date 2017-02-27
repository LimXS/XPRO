import pytest
class Testclass():
    def test_1(self):
        print "test_1"

    def test_2(self):
        print "test_2"


if __name__ == '__main__':
    pytest.main("test_md1_04.py -s ")
