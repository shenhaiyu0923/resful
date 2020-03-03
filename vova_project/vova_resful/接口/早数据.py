import pymysql
import time

conn = pymysql.connect(host='127.0.0.1', port=3306, db='rain', user='root',
                       passwd='123456', charset='utf8')
cur = conn.cursor()


def run111():
    # 常规插入方法
    s = time.time()
    sql = "insert into auth_group (name) values(%s)"
    for i in range(100000):
        cur.execute(sql, [i])


    conn.commit()
    cur.close()
    conn.close()
    e = time.time()

    print(e - s)


def run222():
    # 批量插入方法
    s = time.time()
    data_list = [("ceshi"+str(i),) for i in range(10)]
    print(data_list)
    sql = "insert into auth_group (name) values(%s)"
    total_count = cur.executemany(sql, data_list)
    conn.commit()
    cur.close()
    conn.close()
    e = time.time()

    print(total_count)
    print(e - s)


if __name__ == '__main__':
    #run111()      #7.043838024139404s
    run222()  # 0.6151590347290039s