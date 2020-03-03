*** Settings ***
#Resource  rflib/rc5.robot
Library    pylib.test8
Library    pylib.mylib3


*** Test Cases ***
添加老师
    [Setup]   Run Keywords   list_course
    ...  AND  list_teacher
    ${lesson}   add_course    数学    数学描述    1
    log to console    添加课程返回码${lesson}
    ${tea}  evaluate    [{"id":${lesson['id']},"name":'数学'}]
    ${teach}    add_teacher    zhouyang    周扬password    周扬    周扬123    ${tea}    1
    log to console    老师返回码${teach}
    Should Be True    $teach=={'retcode': 0, 'id': ${teach['id']}}
    ${listc}    list_course
    log to console  课程列表返回码${listc['retlist']}
    ${a}    Convert To Integer   1
    ${dir}      create dictionary  id=${lesson['id']}   name=数学     desc=数学描述   display_idx=${a}
    should contain      ${listc['retlist']}   ${dir}
    Should Be True      $listc['retlist'][0]=={'id': ${lesson['id']}, 'name': '数学', 'desc': '数学描述', 'display_idx': 1}
    should contain      '${listc['retlist']}'   {'id': ${lesson['id']}, 'name': '数学', 'desc': '数学描述', 'display_idx': 1}
    Should Be True      {'id': ${lesson['id']}, 'name': '数学', 'desc': '数学描述', 'display_idx': 1} in ${listc['retlist']}
    printarg    '${listc['retlist']}'
    printarg    ${listc['retlist']}
    printarg    {'id': ${lesson['id']}, 'name': '数学', 'desc': '数学描述', 'display_idx': 1}
    ${listt}    list_teacher
    log to console  老师列表返回码${listt['retlist']}
    Should Be True      $listt['retlist'][0]=={'id': ${teach['id']}, 'realname': '周扬', 'desc': '周扬123', 'display_idx': 1, 'username': 'zhouyang', 'courses': [{'course_id': ${lesson['id']}}]}
   [Teardown]   Run Keywords    del_teacher     ${teach['id']}
    ...  AND  del_course    ${lesson['id']}
#      robot --pythonpath  .  tc



