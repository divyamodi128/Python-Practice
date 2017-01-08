import email
from imaplib import IMAP4_SSL
from bs4 import BeautifulSoup

import os
import mimetypes

username = "divtestpy@gmail.com"
password = "asdfgh111"

mail = IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")

# print mail.list()

result, data = mail.uid('search', None, 'ALL')
# print data

email_list = data[0].split()

for items in email_list:
    result2, email_data = mail.uid('fetch', items, '(RFC822)')
    email_msg = email.message_from_string(email_data[0][1])
    # email_msg = email.message_from_string(email_data[0][1].decode("utf-8"))   # For python 3

    to_ = email_msg['To']
    from_ = email_msg['From']
    sub_ = email_msg['subject']
    if sub_ is None:
        sub_ = "NoSubject"
    date_ = email_msg['date']
    print "From: ", from_
    print "Subject: ", sub_
    print "Date: ", date_
    save_path = os.path.join(os.getcwd(), "emails", date_, sub_)
    print ("Path for Email files:\n", save_path)
    counter = 1
    for part in email_msg.walk():
        # if part.get_content_maintype() == "multipart":
        #     continue
        filename = part.get_filename()
        content_type = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(content_type)
            if not ext:
                ext = ".bin"
            if "text" in content_type:
                ext = ".txt"
            if "html" in content_type:
                ext = ".html"
            filename = "msg-part-%08d%s" %(counter, ext)
        print(filename)
        counter += 1
        # Printing the Emails
        if "plain" in content_type:
            print part.get_payload()
        elif "html" in content_type:
            html_ = part.get_payload()
            soup = BeautifulSoup(html_,"html.parser")
            text_ = soup.get_text()
            print text_.strip()
        else:
            print content_type

        # Saving the contains of email
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, filename), 'wb') as fileobj:
            if ".txt" in filename or ".bin" in filename:
                fileobj.write("From: %s" % (from_))
            # print part.get_payload(decode=True)
            if part.get_payload(decode=True):
                fileobj.write(part.get_payload(decode=True))
    print "----------------------------------------\n"
