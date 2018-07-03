# -*- coding:utf-8 -*-
'''
python SMTP发送邮件，POP3接收邮件 
SMTP协议用于发送邮件，POP3用于接收邮件
'''

from smtplib import SMTP as smtp
from poplib import POP3_SSL as pop  #用POP3_SSL
from time import sleep
from email.mime.text import MIMEText



SMTPServer = 'smtp-mail.outlook.com'
POP3Server = 'pop.qq.com'

origHdrs = ['From:lpb.waln@outlook.com', 'To:m18516292278@163.com', 'Subject:python email test']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])
from_addr = 'lpb.waln@outlook.com'
password = 'Lpb201212'
smtp_server = 'smtp-mail.outlook.com'
to_addr = '773779347@qq.com'
to_user = '773779347'
to_License = 'siyweyavnatgbcbf' #qq邮箱，163邮箱要用授权码登录，授权码在邮箱设置中获取

def sendmail():
    '使用SMTP协议发送邮件'
    serdServer = smtp()
    serdServer.connect(SMTPServer, '587')
    serdServer.starttls()   # 解决SMTP加密问题
    # serdServer.set_debuglevel(1) # 设置日志提示级别
    serdServer.login(from_addr, password)
    errs = serdServer.sendmail(from_addr, to_addr, origMsg)
    print('Mail Send Sucess!')
    serdServer.quit()


def recv_mail():
    '使用POP3_SSL接收邮件，解决邮件安全加密问题'
    print('recving mail...')
    recvServer = pop(POP3Server)
    recvServer.user(to_user)
    recvServer.pass_(to_License)
    rsp, msg, siz = recvServer.retr(recvServer.stat()[0])
    sep = msg.index('')
    recvBody = msg[sep+1:]
    print('Mail_Body:',recvBody)
    assert origBody[0] == recvBody[0]


sendmail()
sleep(10)
recv_mail()