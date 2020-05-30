import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html=Template(Path('python-projects/scripting/index.html').read_text())
email=EmailMessage()
email['from']='Mahabharathi'
email['to']='creatorstudio2k@gmail.com'
email['subject']='you won 1,00,000 dollars!!'

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587)  as smtp:#standard port 587,25
    smtp.ehlo() #protocol of smtp
    smtp.starttls() #Encryption mechanishm
    smtp.login('maha441997@gmail.com','Maha@ravi21')
    smtp.send_message(email)
    print('all good')