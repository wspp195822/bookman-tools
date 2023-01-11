import smtplib
from email.mime.text import MIMEText
from email.header import Header
print("""\033[1;34;40m
      _                 _                          
     | |               | |                         
     | |__   ___   ___ | | ___ __ ___   __ _ _ __  
     | '_ \ / _ \ / _ \| |/ / '_ ` _ \ / _` | '_ \ 
     | |_) | (_) | (_) |   <| | | | | | (_| | | | |
     |_.__/ \___/ \___/|_|\_\_| |_| |_|\__,_|_| |_|                                                                                                     
\033[1;36;40m""")
m_message = '2872646878@qq.com'
password = 'bogffdsjmlgxdheg'
m_message_to = input("邮箱号:")
if(m_message_to == "00"):
    exit()
subject = input("主题:")
text_content = input("正文:")
number = int(input("次数:"))
number_a = 0
msg = MIMEText(text_content,'plain','utf-8')
msg['subject'] = subject
msg['From'] = m_message
msg['To'] = m_message_to
client = smtplib.SMTP_SSL('smtp.qq.com',smtplib.SMTP_SSL_PORT)
client.login(m_message,password)
while(number_a < number):
    number_a += 1
    client.sendmail(m_message,m_message_to,msg.as_string())
    print("send Successful")