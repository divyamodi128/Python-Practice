from smtplib import SMTP, SMTPAuthenticationError, SMTPConnectError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "divtestpy@gmail.com"
password = "asdfgh111"
# from_email = username
to_list = ["divtestpy@gmail.com", "modidivya16@gmail.com"]

email_conn = SMTP(host, port)
print email_conn.ehlo()
print email_conn.starttls()
print email_conn.login(username, password)
# email_conn.sendmail(from_email, to_list, "Hi there, This is a custom Email... \n\n Thank You")
try:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hi There,"
    msg['From'] = username
    # msg['To'] = to_list
    plain_txt = "This is just a plain txt."
    html_txt = """
    <html>
      <body>
        <h3>Hello World!</h3>
        <p>Testing this email <b>messages</b>. Made By <a href="#">Divya Modi</a>.</p>
      </body>
    </html>
    """
    part1 = MIMEText(plain_txt, 'plain')
    part2 = MIMEText(html_txt, 'html')
    msg.attach(part1)
    msg.attach(part2)
    print str(msg)
    email_conn.sendmail(username, to_list, str(msg))
except SMTPAuthenticationError:
    print "Authentication Error Occurred."
except:
    print "Some Error Occurred"
finally:
    email_conn.quit()

