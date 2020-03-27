import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtp_host = 'smtp.qq.com'
sender = '1206290545@qq.com'
password = "tsgowtbewkltjgfh"


def send_mail(to, title, subject):
    server = smtplib.SMTP(smtp_host, 25)
    server.login(sender, password)
    msg = MIMEText(subject, 'plain', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    for receiver in to:
        msg['To'] = Header(receiver)
        server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print('send success by port 25')
