import paramiko

#创建SSHClint实例对象
ssh=paramiko.SSHClient()

#调用方法,表示没有存储远程机器的公钥,允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器 地址 端口 用户名 密码
#ssh.connect("192.168.85.139",22,"pear","pear")
ssh.connect("192.168.85.157",22,"pear","pear")
cmd='ls'
#cmd='mkdir /root/Desktop/test'
stdin,stdout,stderr=ssh.exec_command(cmd)
print(stdout.read().decode())
#创建目录
# cmd = 'mkdir jcy2'
# ssh.exec_command(cmd)

#如果命令跨行
# cmd = '''echo '1234
# 5678 > myfile
# abcd'
# '''
# ssh.exec_command(cmd)

#获取命令的执行结果
# cmd='cat myfile'
# stdin,stdout,stderr=ssh.exec_command(cmd)
# output=stdout.read()+stderr.read()
# print(output.decode('utf8'))
ssh.close()



# sftp=ssh.open_sftp()#上传文件
# sftp.put('ftp3.py','/home/aa/ftp3.py')
# sftp.close()
# ssh.close()

# sftp=ssh.open_sftp()#下载文件
# sftp.get('/home/aa/ftp3.py','e:/aa/ftp3.py')
# sftp.close()
# ssh.close()





