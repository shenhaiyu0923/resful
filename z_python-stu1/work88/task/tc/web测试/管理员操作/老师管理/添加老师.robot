*** Settings ***
#Resource  rflib/rc5.robot
Library    pylib7.WebOpAdmin
Variables  cfg5.py
Library    SeleniumLibrary
Library    Collections




*** Test Cases ***
添加老师

    [Setup]   Run Keywords   deleteAllt
    ...  AND  deleteAllc
    ...  AND  增加课程   初中语文    初中语文描述    1
    [Teardown]  run keywords  deleteAllt    AND     deleteAllc
    增加老师   庄子    zhuangzi    庄子老师   1   初中语文
    ${teachers}   检查老师
    Should Be True    $teachers==[u'庄子']




