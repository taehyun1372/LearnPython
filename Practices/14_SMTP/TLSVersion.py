import smtplib

server = "172.253.118.109"
port = 587

with smtplib.SMTP(server, port) as smtp:
    smtp.set_debuglevel(1)

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("xogus1372@gmail.com", "lqbh spsm rawv yrui")

    msg = "Subject: Test\n\nHello TLS email!"
    smtp.sendmail("xogus1372@gmail.com", "taehyun1372@naver.com", msg)
