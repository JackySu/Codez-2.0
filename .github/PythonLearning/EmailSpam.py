import os
import smtplib
import time
import random
from email.mime.text import MIMEText


def mix_content():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(7):
        sa.append(random.choice(seed))
    content = ''.join(sa)
    return content


from_addr = "723447190@qq.com"
password = "pjpmzojrqmvkbgab"

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:1080'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1080'
qnum = input("Enter QQ number: ")
times = int(input("Enter times the email would send: "))
to_addr = qnum + "@qq.com"

smtp_server = "smtp.qq.com"

server = smtplib.SMTP_SSL(smtp_server)

server.connect(smtp_server, 465)
server.login(from_addr, password)

for i in range(times):
    SleepTime = random.random() * 10
    time.sleep(SleepTime)
    msg = MIMEText(mix_content(), "plain", "utf-8")
    server.sendmail(from_addr, to_addr, msg.as_string())

server.quit
