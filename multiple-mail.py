
import smtplib

file = open("maillist","+r")
# if you have a mail list, can use the line above
# first parameter = file and path, second parameter = read the file
# Example Usage = file = open("/home/user/maillist.txt","+r")


content = "mail content"

mail = smtplib.SMTP("smtp.<mail_server>",587)
# first parameter = mail server, second parameter = port
# Example usage = mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()
# Identify yourself to an SMTP server

mail.starttls()
# Encrypted to Content

mail.login("sender mail account","accounts password")
# first parameter = mail account, second parameter = password
# Example Usage = mail.login("mymail@gmail.com","1234")

mailaccounts = file.readlines()

for i in mailaccounts:
    mail.sendmail("sender mail account",i,content)
