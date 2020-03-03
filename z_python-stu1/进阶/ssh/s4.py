import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "Songqin123")

cmd = "pwd;mkdir jcy4;cd jcy4;pwd;mkdir jcy44"
stdin, stdout, stderr = ssh.exec_command(cmd)

print(stdout.read().decode())
ssh.close()


