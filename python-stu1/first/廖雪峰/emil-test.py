import smtplib
from email.mime.text import MIMEText

email_host = 'smtp.qq.com'     #邮箱地址  pop3  ，smtp
email_user = '192137089@qq.com'  # 发送者账号
email_pwd = 'uznpcyddbpkmbjbd'  # 发送者的密码:uznpcyddbpkmbjbd    这个是开启邮箱第三方登陆授权码
maillist ='1802161998@qq.com'  #收件人邮箱，多个账号的话，用逗号隔开

msg = MIMEText('这是个python测试邮件，不用回复。')    # 邮件内容
msg['Subject'] = 'python主题'    # 邮件主题

smtp = smtplib.SMTP(email_host,port=25) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
smtp.sendmail(email_user, maillist, msg.as_string())
# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('email send success.')