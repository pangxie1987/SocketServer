#-*- coding:utf-8 -*-
'''
调用邮箱服务器，发送邮件
'''

import string
import sys
from PIL import ImageGrab
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email import encoders
from ScreenShot import Screenshot
from email.mime.application import MIMEApplication
from PyKSZeroTest_Gold.contdata import const

# 将下列文件目录加载进来
sys.path.append('../')

def toSendMail():

    msg=MIMEMultipart()

    smtpserver='smtp-mail.outlook.com' #发送服务器
    port='587'
    #user='m18516292278@163.com'
    user='lpb.waln@outlook.com'  #发送邮箱用户
    passwd='Lpb201212'

    sender='lpb.waln@outlook.com' #发送邮箱地址

    # reverser='pingbao.liu@fisglobal.com'  #接收邮箱
    reverser='pingbao.liu@fisglobal.com,'
             #'jiabing.chen@fisglobal.com,guangshen.duan@fisglobal.com'
    reverser = string.splitfields(reverser, ",")

    subject=r'Python Mail Test with attach-邮件主题!'  #主题中带中文的，则发件人名称正常


    #邮件主题
    #msg=MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
    msg['Subject']=Header(subject,'utf-8')

    # 邮件内容正文
    msg.attach(MIMEText(r'Zero项目自动化测试运行结果'))

    #添加附件
    # filename="photo.png"
    # sendfile=open('geckodriver.log','a+').read()
    # att=MIMEText(sendfile,'base64','utf-8')
    # att["Content-Type"]='application/octet-stream'
    # att['Content-Disposition']='attchment;filename=%s'%filename.encode('gb2312')
    # msgRoot=MIMEMultipart('related','utf-8')
    # msgRoot['Subject']=subject
    # msgRoot.attach(att)

    # 调用截图函数 进行截图
    #Screenshot()

    # # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    # with open('photo.png', 'rb') as f:
    #     # 设置附件的MIME和文件名，这里是png类型:
    #     mime = MIMEBase('image', 'png', filename='photo.png')
    #     # 加上必要的头信息:
    #     mime.add_header('Content-Disposition', 'attachment', filename='photo.png')
    #     mime.add_header('Content-ID', '<0>')
    #     mime.add_header('X-Attachment-Id', '0')
    #     # 把附件的内容读进来:
    #     mime.set_payload(f.read())
    #     # 用Base64编码:
    #     encoders.encode_base64(mime)
    #     # 添加到MIMEMultipart:
    #     msg.attach(mime)

    # 把测试报告的附件加载进来

    part=MIMEApplication(open(const.testreport,'rb').read())
    print('attach-testreport',const.testreport)
    part.add_header('Content-Disposition','attachment',filename='Autotest_result.xlsx')
    msg.attach(part)

    # 将测试案例的附件加载进来
    part = MIMEApplication(open(const.testcasecp, 'rb').read())
    print('attach-testcasecp',const.testcasecp)
    part.add_header('Content-Disposition', 'attachment', filename='Autotest_case.xlsx')
    msg.attach(part)

    smtp=smtplib.SMTP()

    smtp.connect(smtpserver,port)  #使用port
    smtp.starttls() #SMTP 加密方法 STARTTLS  解决加密问题
    smtp.ehlo()
    smtp.login(user,passwd)
    smtp.sendmail(sender,reverser,msg.as_string())
    smtp.quit()
    print('Email send Sucess!')

# toSendMail()