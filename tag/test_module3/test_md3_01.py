#*-* coding:UTF-8 *-*
from  tagconfig import setfix
import pytest



class Testclass():

    def test_one(self,c):
        print('Testmd3_01_11 called.')

        #print m+1

    def test_two(self):
        print('Testmd3_01_12 called.')
        #print m+1


class Testclass2():
    def test_one2(self):
        print('Testmd3_01_21 called.')

    def test_two2(self):
        print('Testmd3_01_22 called.')

if __name__ == '__main__':
    pytest.main("-d --tx 2*popen --html=../report.html ../test_module1/test_md1_03.py")