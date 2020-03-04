import pytest
from p4.pylib.ApiSchoolClass import ins_ApiSchoolClass
from p4.pylib.ApiTeacher import  ins_ApiTeacher

@pytest.fixture(scope='package',autouse=True)
def st_clearAll(request):
    print(f'\n---初始化::构建空白数据环境')

    # 初始化代码
    ins_ApiTeacher.delete_all_teacher()
    ins_ApiSchoolClass.delete_all_school_class()
    def fin():
        print(f'\n---清除：：清除空白数据环境')
    request.addfinalizer(fin)

#  pytest -s tc  --html=report1.html
