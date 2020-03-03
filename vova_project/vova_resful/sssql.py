from pymysql import connect

def main():

    # 创建Connection连接
    conn = connect(host='localhost',port=3306,user='root',password='123456',database='yuyan',charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    params = ['ming','ning']
    # 执行select语句，并返回受影响的行数：查询所有数据
    #count = cs1.execute("select * from goods where name=%s or name=%s", params)
    count = cs1.execute("select * from goods where name='{}'".format('ming'))

    print(count)
    # 获取查询的结果
    # result = cs1.fetchone()
    result = cs1.fetchall()
    # 打印查询的结果
    print(result)
    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()

if __name__ == '__main__':
    main()