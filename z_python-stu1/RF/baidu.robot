#coding=utf-8
*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
baidu
    Open Browser                  http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=kw                   清华\n
    ${firstRet}                   Get Text                id=1
    Should Contain                ${firstRet}             清华
    close browser


