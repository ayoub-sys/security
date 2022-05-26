#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email import encoders 
import smtplib 
import os 
from  email.message import EmailMessage 
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    
    smtp.ehlo()
    smtp.starttls() 
    #subject='python for cyber security'
    #body='Hello Ayoub This Is My First Email using python'
    sender="khlifiayoob@gmail.com"
    #receiver="khlifiayoob@gmail.com"

    """------alternative ay more orgaisable----
    msg=EmailMessage()
    msg['Subject']='python for cyber security'
    msg['From']="khlifiayoob@gmail.com"
    msg['To']="khlifiayoob@gmail.com"
    msg.set_content('How about your content')
    #msg.add_attachment() """
    
    smtp.login(sender,"enicarthage555")
    #msg=subject+"\n"+"\n"+body
    smtp.send_message(msg)   #or smtp.sendmail(sender, receiver, msg) 
