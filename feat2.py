import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import filedialog as fd

email_user = 'email_id'
email_password = 'email_password'
subject = "Confirmation Email"
Body = "Hello {}, thank you for registering. Your feedback is valuable to us. Please login and review the mobiles."
def mail(email_send, user_name, file_path=None):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject.format(user_name)
    body = Body.format(user_name)
    
    msg.attach(MIMEText(body,'plain'))
    if file_path is not None:
        for each_file in file_path:
            try:
                attachment  = open(each_file,'rb')
                
                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                sudo_filename = each_file.split('/')[-1]
                
                part.add_header('Content-Disposition',"attachment; filename= "+sudo_filename)
                msg.attach(part)
            except:
                print("Unable to attach file")
    else:
        print("No file")
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()