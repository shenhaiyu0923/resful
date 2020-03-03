#!/usr/bin/python3
import pytest
import time
curtime=time.strftime("%Y%m%d-%H%M%S", time.localtime())
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
if __name__=='__main__':
    pytest.main(['-s',  #-q去除多余输出参数
                 'p7/tc',  #文件路径
                 '--html=report/ %s test.html' % curtime,  #路径和输出格式
            #     '--junitxml=report/ %s log.xml' % curtime,
                 ])

    #pytest tc -s --html = report1.html
    #py.test test_class.py --resultlog =./ log / log.txt

