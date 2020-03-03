a={"admin":"111","pwd":"123"}
sum = 1
def login(sum):
    c=input("请输入用户名:")
    d=input("请输入密码:")
    if c==a["admin"] and d==a["pwd"]:
        print("登录成功,欢迎"+c+"来到松勤课堂")
        login(sum)
    else:
        if sum <3:
            sum+=1
            login(sum)
        else:
            print("您已连续三次输入错误,账号被冻结")
login(sum)