*** Settings ***
Library  mylib3.py



*** Test Cases ***
测试
    ${var}    set variable   hello      #赋值
#    ${var}      convert to integer      #传递证书
    ${var}      create list     a  b  c
    ${list2}   returnlist
    ${dict2}    returndict
    printarg    ${list2}
    printarg    @{list2}[0]  #取列表
    printarg    &{dict2}[ele1]   #取字典

    printarg   ${var}
    Log To Console    变量var的值为：${var}
#    Should Be Equal   ${var}   helle   搜索 python判断









