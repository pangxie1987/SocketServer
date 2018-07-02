# -*- coding:utf-8 -*-
'''
ftp连接客户端ftplib
'''

import ftplib, os, socket

# host = 'ftp.mozilla.org' # ftp Server地址
host = 'ftp.scene.org'
dirn = 'music/groups/2063music/'  # 目标文件目录
file = '63_001-opal2000-gatev0-5.mp3' # 目标文件名称

def main():
    '''
    ftp形式访问ftp.scene.org，并下载目录下的文件
    '''
    try:
        f = ftplib.FTP(host)
        f.set_pasv(False)
    # except (socket.error, socket.gaierror), e:
    #     print("ERROR:cant't reach %s" %host)
    except Exception as e:
        print e
        return
    print("***Connected to host %s"%host)

    try:
        f.login()
    except ftplib.error_perm:
        print("ERROR:cannot login anonymously")
        f.quit()
        return
    print("***Logged in as 'annonymous'")
    
    try:
        f.cwd(dirn)
    except ftplib.error_perm:
        print("ERROR:cannot CD to %s"%dirn)
        f.quit()
        return
        print("***Changed to %s folder"%dirn)

    try:
        f.retrbinary('RETR %s'%file, open(file, 'wb').write)
    except ftplib.error_perm:
        print("ERROR:cannot read file %s"%file)
        # os.unlink(file)  # os.unlink()用于删除文件
    else:
        print("***Download %s to CWD"%file)
        f.quit()
        return

if __name__ == '__main__':
    main()
    

