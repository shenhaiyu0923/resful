*** Settings ***
Library  SeleniumLibrary
Variables  cfg5.py


*** Variables ***
#&{user}     name=auto   pwd=sdfsdfsdf

#${username}     auto
#${password}     sdfsdfsdf

${url}          http://localhost/mgr/login/login.html

*** Keywords ***
setup webtest
    open browser  http://localhost/mgr/login/login.html  chrome
    set selenium implicit wait  3

teardown webtest
    close browser


登录
    go to   ${url}
    set selenium implicit wait  3
#    input text  id=username     ${username}
#    input text  id=password     ${password}

    input text  id=username     &{user1}[name]
    input text  id=password     &{user1}[pwd]

#    input text  id=username     &{user}[name]
#    input text  id=password     &{user}[pwd]
    click element  css=.btn-success
退出
    click element  css=[ng-click="logout()"]
    click element   css=.header-content



增加课程
    [Arguments]   ${name}   ${desc}   ${idx}
    click element   css=[ng-click="showAddOne=true"]
    input text      css=[ng-model="addData.name"]       ${name}
    input text      css=[ng-model="addData.desc"]       ${desc}
    input text  css=[ng-model="addData.display_idx"]  ${idx}
    click element  css=[ng-click="addOne()"]
    click element  css=[ng-click="$parent.showAddOne=false"]
    sleep  1

检查课程
    [Arguments]     ${name}
    ${eles}     Get WebElements    css=tbody td:nth-child(2)
    ${courses}  evaluate        [ele.text for ele in $eles]
    should be true  $name in $courses

增加老师
    [Arguments]   ${realname}   ${username}   ${desc}    ${idx}    ${course}
    click element  css=[ui-sref="teacher"]
    click element   css=[ng-click="showAddOne=true"]
    input text      css=input[ng-model='addEditData.realname']    ${realname}
    input text      css=input[ng-model='addEditData.username']    ${username}
    input text      css=textarea[ng-model='addEditData.desc']    ${desc}
    input text      css=input[ng-model='addEditData.display_idx']    ${idx}
    Select From List By Label   css=select[ng-model*=courseSelected]    ${course}
    Click Element    css=button[ng-click*=addTeachCourse]
    Click Element   css=button[ng-click^=addOne]
    click element  css=[ng-click="$parent.showAddOne=false"]
    sleep   1

检查老师

    Click Element   css=ul.nav a[href*=teacher]
    ${eles}    Get Webelements    css=tr>td:nth-child(2)
    ${teachers}    evaluate     [ele.text for ele in $eles]
    [Return]   ${teachers}


deleteAllt
    click element  css=[ui-sref="teacher"]
    set selenium implicit wait  3
    FOR   ${one}     IN   RANGE     9999
        ${del_btns}     get webelements    css=[ng-click="delOne(one)"]
        exit for loop if  $del_btns==[]
        evaluate  $del_btns[0].click()
        sleep  1
        click element  css=.btn-primary
        sleep  1
    END


deleteAllc
    set selenium implicit wait  3
    click element  css=[ui-sref="course"]
    FOR   ${one}     IN   RANGE     9999
        ${del_btns}     get webelements    css=[ng-click="delOne(one)"]
        exit for loop if  $del_btns==[]
        evaluate  $del_btns[0].click()
        sleep  1
        click element  css=.btn-primary
        sleep  1
    END

