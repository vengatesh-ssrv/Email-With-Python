import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

print("\n")
print("*************Gmail deatails******************")
email_user = input("Gmail-id===>")
email_password = getpass.getpass(prompt='Enter Password===>')
print("**********************************************")
print("\n")

print("****************List of recievers**************")
file1 = open("gmail.txt", "r") 
listt=file1.read() 
list1=str.split(listt,",")
send=[]
for i in range(0,len(list1)):
    if list1[i]!="\n":
        send.append(list1[i])

print(send)
print("***********************************************")
print("\n")

print("*****************Content of Mail***************")
subject = input('subject for your mail===>')
body = input('Body/Content for your mail===>')
filename=input("Filename to be attached===> ")
print("************************************************")
print("\n")

print("****************Mail Started to sent*************")
for i in range(0,len(send)):
    email_send=send[i]
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    msg.attach(MIMEText(body,'plain'))

    attachment  =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
    print("no. of mail sent:",i+1,"Username:",send[i])

print("************************************************")
