# -*- coding:utf-8 -*-
'''
使用paramiko库实现sftp的登录及文件的传输和执行命令
'''

import paramiko, os

class SFTP(object):
    def __init__(self):

        self.host ='10.243.140.219'
        self.user='kfts'
        self.passwd='kfts'
        self.port = 22
        self.remote_dir = '/home/kfts/its/data_sync/'
        self.local_dir = "C:\Users\pingbao.liu\Desktop\log"
        # 连接及登录部分
        try:
            self.t = paramiko.Transport(self.host, self.port)
            self.t.connect(username=self.user, password=self.passwd)
            self.sftp = paramiko.SFTPClient.from_transport(self.t)
        except Exception as e:
            print e

    def down_files(self):
        '''
        使用get方法将远程文件下载到本地
        '''
        files = self.sftp.listdir(self.remote_dir)    # 列出remote_dir 目录下的所有文件， 返回文件名列表
        print(files)
        for file in files:
            # print(file)
            try:
                self.sftp.get(os.path.join(self.remote_dir, file), os.path.join(self.local_dir, file)) # 使用get方法将远程文件下载到本地
            except Exception as a:
                print a
            else:
                print('%s download sucess!'%file)
        print('all download done! ')
        self.t.close()

    def upload_files(self):
        '使用put方法上传本地文件到远程服务器'
        try:
            files = os.listdir(self.local_dir)
            print(files)
            for file in files:
                self.sftp.put(os.path.join(self.local_dir, file), os.path.join(self.remote_dir, file))
                print('%s upload sucess!'%file)
            print('all upload sucess!')
            self.t.close()
        except Exception as b:
            print b

    def execute_command(self):
        '使用SSHClient()函数，在远程机器上执行命令'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, username=self.user, password=self.passwd)
        stdin, stdout, stderr = ssh.exec_command("cd /home/kfts/its/data_sync/logs;mkdir test")
        print(stdout.readlines())
        print(stderr.readlines())
        ssh.close()

if __name__ == '__main__':
    sftptest = SFTP()
    sftptest.execute_command()
