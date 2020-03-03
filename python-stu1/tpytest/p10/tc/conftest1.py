import pytest
from p10.pylib.ApiTeacher import  ins_ApiTeacher
from p10.pylib.ApiTeacher import  ins_ApiTeacher
from p10.pylib.ApiSchoolClass import ins_ApiSchoolClass
from p10.pylib.MobileAdmin import ins_MobileAdmin
from p10.pylib.WebTeacher import ins_WebTeacher
@pytest.fixture(scope='package',autouse=True)
def st_clearAll():
    print(f'\n---初始化::构建空白数据环境')

    # 初始化代码
    ins_ApiTeacher.delete_all_teacher()
    ins_ApiSchoolClass.delete_all_school_class()

