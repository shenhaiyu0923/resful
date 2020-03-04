测试套件文件
s1.robot
** *Settings ** *
Library
SeleniumLibrary
Library
course_mgr
Library
Collections

** *Test
Cases ** *
测试1
${courseList} = ListCourse
:FOR   ${ele}
IN @ {courseList}
\    log
to
console   ${ele}


${expected} = Create
List
python语言
初中化学
Lists
Should
Be
Equal     ${courseList}     ${expected}

测试2
Open
Browser
https: // www.vmall.com / chrome
Set
Selenium
Implicit
Wait
4
${eles} = Get
Webelements
css =.home - hot - goods.grid - items: not (.grid-items-sm)
div
:FOR   ${ele}
IN @ {eles}
\   log
to
console   ${ele.text}
\   ${eletxt} = evaluate  $ele.get_attribute('innerText')
\   log
to
console   ${eletxt}

Close
Browser