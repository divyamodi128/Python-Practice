from smtplib import SMTP, SMTPAuthenticationError, SMTPConnectError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

import os

host = "smtp.gmail.com"
port = 587
username = "youremail@gmail.com"
password = "yourpassword"
file_ = "templates/email_html_templates.html"


def get_templates_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("File path is invalid %s" % (file_path))
    return file_path


def get_templates(path):
    file_path = get_templates_path(path)
    return open(file_path).read()


def render_context(templates_string, context):
    return templates_string.format(**context)


class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = get_templates(file_) # fetch messages from txt file

    def add_user(self, name, amount, email=None):
        detail = {
            "name": name[0].upper() + name[1:].lower(),
            "amount": "%.2f" % (amount),
            "date": '{today.month}/{today.day}/{today.year}'.format(today=datetime.date.today()),
        }
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)

    def get_user(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details):
            for detail in self.get_user():
                new_msg = render_context(self.base_message, detail)
                # new_msg = self.base_message.format(
                #     name=detail["name"],
                #     amount=detail["amount"],
                #     date=detail["date"],
                # )
                user_email = detail.get("email")
                if user_email:
                    user_details = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_details)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []

    def send_emails(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail["email"]
                user_message = detail["message"]
                # run Email
                try:
                    email_conn = SMTP(host, port)
                    print email_conn.ehlo()
                    print email_conn.starttls()
                    print email_conn.login(username, password)
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "Hi There,"
                    msg['From'] = username
                    msg['To'] = user_email

                    if '.txt' in file_:
                        part1 = MIMEText(user_message, 'plain')
                    else:
                        part1 = MIMEText(user_message, 'html')

                    msg.attach(part1)
                    # print "msg", str(msg)
                    email_conn.sendmail(username, [user_email], str(msg))
                except SMTPAuthenticationError:
                    print "Authentication Error Occurred."
                except:
                    print "Some Error Occurred"
                finally:
                    email_conn.quit()
            return True
        return False


obj = MessageUser()
obj.add_user('diVya', 15.36, email="modidivya16@gmail.com")
obj.add_user('pAlak', 23.548, email="divyamodi128@outlook.com")
obj.add_user('praNav', 56.4623, email="divtestpy@gmail.com")
obj.add_user('dhwanil', 10.00, email="divtestpy@gmail.com")
obj.add_user('mauLIK', 135.5, email="divtestpy@gmail.com")
print obj.get_user()
# print obj.make_messages()
print obj.send_emails()
