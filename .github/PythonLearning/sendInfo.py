# -*- coding: UTF-8 -*-
# sendInfo.py
# !/usr/bin/env python						# 在环境变量中找python编译器
# _*_coding:utf8_*_
import smtplib, config, email, sys, socket, threading, time  # 导入包，以及config文件
import random
import string
from email.Message import Message


def connect():
    try:
        server = smtplib.SMTP(config.smtpServer,
                              config.smtpPort)  # 创建SMTP对象，链接自己邮箱的smtp服务器
        server.ehlo()  # 向smtp服务器打招呼，链接到服务器成功的话，会返回一个元组，第一项为250
        server.login(config.smtpUser, config.smtpPwd)  # 登录自己的邮箱，返回值是235表示认证成功
        return server
    except Exception:
        print("无法连接到邮箱服务器！")


def sendInfo(server, to, subject, content):
    # 设置邮件格式和内容
    msg = Message()
    msg['Mime-Version'] = '1.0'
    msg['From'] = config.smtpUser  # 设置邮件的发送人
    msg['To'] = to  # 设置邮件的接收人
    msg['Subject'] = subject  # 设置邮件的标题
    msg.set_payload(content)  # 设置邮件的正文
    try:
        mailinfo = server.sendmail(config.smtpUser, to,
                                   str(msg))  # 用sendmail函数发送邮件
    except Exception as ex:
        print("Error!邮件发送失败！%s" % ex)
    else:
        print("Goodluck！邮件发送成功！")


def myfunc():
    global contents
    print(contents)
    text = "你好"
    if contents != text:
        contents = text
        server = connect()
        sendInfo(server, to, subject, contents)
    t = threading.Timer(10, myfunc)
    t.start()


if __name__ == '__main__':
    while True:
        to = config.sendTo  # 从config文件中获取收件人地址
        subject = "测试"  # 设定邮件的主题
        server = connect()
        # seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        # sa = []
        # for i in range(8):
        # sa.append(random.choice(seed))
        contents = "你好"  # 邮件的内容
        # contents = ''.join(sa)
        print(contents)
        sendInfo(server, to, subject, contents)  # 开始发送邮件
        timer = threading.Timer(10.0, myfunc)  # 设定定时器，10秒后执行myfunc函数
        timer.start()  # 开始执行线程
        time.sleep(1)
'''
#_*_coding:utf8_*_
#config.py 
smtpServer='smtp.qq.com' #邮件发送帐户的smtp服务器地址
smtpPort='465' #邮件发送帐户的smtp服务器发送端口
smtpUser='@qq.com' #邮件发送帐户名
smtpPwd='****' #邮件发送帐户密码，我这里打*号
sendTo='****@qq.com' #接收邮箱地址
'''
