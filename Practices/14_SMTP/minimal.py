import smtplib

server = "172.253.118.109"    # or your SMTP server IP
port = 25               # plain SMTP

with smtplib.SMTP(server, port) as smtp:
    smtp.set_debuglevel(1)  # <-- This prints every command and response!

    from_addr = "xogus1372@gmail.com"
    to_addr = "taehyun1372@naver.com"
    message = """\
From: xogus1372@gmail.com
To: taehyun1372@naver.com
Subject: Test

Hello, SMTP!
"""

    smtp.sendmail(from_addr, [to_addr], message)
