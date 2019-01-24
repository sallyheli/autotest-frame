#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

ContactList = [
    '453421307@qq.com',
    '412277685@qq.com',
    'helili1991@163.com']

def sendEmail():
    message = MIMEMultipart()
    message['From'] = Header("hel<453421307@qq.com>")
    message['To'] = Header(";".join(ContactList))
    message['Subject'] = Header("这是测试结果的反馈","utf-8")

    message.attach(MIMEText('查阅附加','plain','utf-8'))
    att = MIMEText(open("./testResult.html").read())
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="testResult.html"'
    message.attach(att)

    mailHost = "smtp.qq.com"
    name = "453421307@qq.com"
    password = "ysjgdmsqcztqcaih"

    sender = "453421307@qq.com"
    #receive = ";".join(ContactList)
    #print receive

    try:
        smtp = smtplib.SMTP()
        smtp.connect(mailHost,25)
        smtp.login(name,password)

        smtp.sendmail(sender,ContactList,message.as_string())
    except smtplib.SMTPException,e:
        print e
if __name__ == "__main__":
    sendEmail()