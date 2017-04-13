import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Log in
server.ehlo()
server.starttls()
server.login("You@email.com", "yourpassword")

#send the mail
msg = "\LOLLOLL!"
# the \n seperates the message from the headers

#loop if you want to send sevwral eemail
#for i in range(0,10):
server.sendmail("you@mail.com", "target@mail.com", msg)
