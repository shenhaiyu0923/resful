import pytest
from p5.pylib.ApiSchoolClass import ins_ApiSchoolClass

@pytest.fixture(scope='package',autouse=True)
def st_g7c1(request):
    print(f'\n---初始化::创建7年级1班\n')

    # 初始化代码
    ret = ins_ApiSchoolClass.add_school_class(1,
                                        '1班',
                                        60)

    def fin():
        # 清除代码
        print(f'\n---清除::删除7年级1班\n')
        ins_ApiSchoolClass.delete_school_class(ret['id'])


    request.addfinalizer(fin)

    return {'id' : ret['id']}

