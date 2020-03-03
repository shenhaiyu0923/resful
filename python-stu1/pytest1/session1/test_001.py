

def add(x):
    return x+2
class Testa():
    def test_add1(self):
        print()
        print('case001开始')
        assert add(3) == 4
        print('case001结束')
    def test_add2(self):
        print()
        print('case002开始')
        assert add(3) == 5
        print('case002结束')
#           pytest testfirst.py

#           pytest tc -s


#           pip install pytest-html
#           pytest tc -s --html=report1.html