import smtplib

fromaddr = 'shravyacore@gmail.com'
toaddrs  = 'aneeshashutosh@gmail.com'
msg = 'test'
username = 'shravyacore@gmail.com'
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()

server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
