
import smtplib
#smtplib这个模块是管发邮件
from email.mime.text import MIMEText
#构造邮件内容
from email.mime.multipart import MIMEMultipart
#发带附件的邮件用的
email_host = 'smtp.qq.com'     #邮箱地址  pop3  ，smtp
email_user = '192137089@qq.com'  # 发送者账号
email_pwd = 'ibodxgbaneitcaei'  # 发送者的密码:uznpcyddbpkmbjbd    这个是开启邮箱第三方登陆授权码
maillist ='1802161998@qq.com'  #收件人邮箱，多个账号的话，用逗号隔开


new_msg = MIMEMultipart()#构建了一个能发附件的邮件对象
new_msg.attach(MIMEText('这是Python测试发邮件的邮件，不要回复'))# 邮件内容
new_msg['Subject'] = 'Python测试邮件带附件'    # 邮件主题


new_msg['From'] = email_user    # 发送者账号
new_msg['To'] = maillist    # 接收者账号列表
att = MIMEText(open('C:/study/youjian.txt').read())
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="haha.txt"'
new_msg.attach(att)
smtp = smtplib.SMTP(email_host,port=25) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
smtp.sendmail(email_user, maillist, new_msg.as_string())

# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('email send success.')