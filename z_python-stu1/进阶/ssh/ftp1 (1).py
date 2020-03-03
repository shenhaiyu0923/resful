import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "Songqin123")


sftp = ssh.open_sftp()
sftp.put('ftp1.py', '/home/stt/ftp1.py')
sftp.close()

ssh.close()
