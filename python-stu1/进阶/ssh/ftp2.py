import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "Songqin123")

sftp = ssh.open_sftp()
sftp.get('/home/stt/myfile', 'd:/myfile1.txt')
sftp.close()


ssh.close()
