from fabric2 import Connection

class Ssh():
    def __init__(self,ip,username,password):
        self.conn = Connection(f"{username}@{ip}", connect_kwargs={"password": f"{password}"})
    def execute_cmd(self,cmd):
        return self.conn.run(cmd)

def deploy():
    # 如果服务器配置了ssh免密码登录，就不需要 connect_kwargs 来指定密码
    conn = Connection("root@192.168.1.62", connect_kwargs={"password": "1qaz#EDC"})
    # conn.run("top -n 1 > temp.txt")
    conn.run("vmstat")
    #
    # with conn.cd('/home'):
    #     conn.run("mkdir testdir")
    # with conn.cd('/home/testdir'):
    #     conn.run('mkdir aaa')
    #     conn.put('test', '/home/testdir')  # 上传文件


if __name__ == '__main__':
    s = Ssh('192.168.4.101','root','1qaz#EDC')
    m = s.execute_cmd('ls')
    print(m)