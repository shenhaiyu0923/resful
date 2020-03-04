import pytest
from p5.pylib.ApiSchoolClass import ins_ApiSchoolClass
from p5.pylib.ApiTeacher import  ins_ApiTeacher

@pytest.fixture(scope='package',autouse=True)
def st_clearAll():
    print(f'\n---初始化::构建空白数据环境')

    # 初始化代码
    ins_ApiTeacher.delete_all_teacher()
    ins_ApiSchoolClass.delete_all_school_class()

