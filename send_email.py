#coding for sending message through gamil

from email.mime.text import MIMEText
import smtplib   #importing server for gmail

def send_email(email):   #note fn name and file name are same (no problem in this)
    from_email="mohdarif25636@gmail.com"
    from_password="Bismillah786@"
    to_email=email

    subject="Height data"
    message="hey your height is  <strong>%s</strong>" %height

    msg=MIMEText(message, 'html')  #telling gmail that our message is a type of html text
    msg["Subject"]=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)   #server for gamil
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)  #loginng in gmail
    gmail.send_message(msg) #sending meassage


