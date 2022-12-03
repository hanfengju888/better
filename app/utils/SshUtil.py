import paramiko


class SSHLinux():
    def __init__(self, hostname, port, username, password):
        # 创建sshClient实例对象
        ssh = paramiko.SSHClient()
        # 设置信任远程机器，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh = ssh
        self.ssh.connect(hostname, port=port, username=username, password=password)

    def use_command(self, cmd):
        try:
            """
            stdin  标准格式的输入，是一个写权限的文件对象
			stdout 标准格式的输出，是一个读权限的文件对象
			stderr 标准格式的错误，是一个写权限的文件对象”
			执行命令会返回三个对象，调用一次exec_command方法就相当于重新打开一次linux终端
			"""

            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            print(stderr.read().decode())
            res = stdout.read().decode()
            return res
        except Exception as e:
            print(e)
            self.ssh.close()

#
# hostname = "192.168.4.101"
# port = 22
# username = "root"
# password = "1qaz#EDC"
# ssh = SSHLinux(hostname, port=port, username=username, password=password)
# print(ssh.use_command("ps -ef|wc -l"))
