dict={"admin":"111","pwd":"123"}
while True:
    admin=input("请输入用户名")
    if admin==dict["admin"]:
        for i in [2,1,0]:
            passwd = input("请输入密码")
            if passwd != dict[admin]:
                passwd = input("密码错误,请重新输入")
                print("还有"+str(i)+"次机会")
            elif passwd==dict[admin]:
                print("登录成功")
                break
        break






