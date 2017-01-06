import email
from imaplib import IMAP4_SSL

username = "divtestpy@gmail.com"
password = "asdfgh111"

mail = IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")

print mail.list()

result, data = mail.uid('search', None, 'ALL')
print data

inbox_item_list = data[0].split()
oldest_mail = inbox_item_list[0]
newest_mail = inbox_item_list[-1]

result2, oldest_mail_data = mail.uid('fetch', oldest_mail, '(RFC822)')
result3, newest_mail_data = mail.uid('fetch', newest_mail, '(RFC822)')

raw_old_email = oldest_mail_data[0][1] # .decode("utf-8")   (for python 3 users)
print raw_old_email
raw_new_email = newest_mail_data[0][1]
print raw_new_email

new_email_msg = email.message_from_string(raw_new_email)
print new_email_msg

print 'To:', new_email_msg['To']
print 'From:', new_email_msg['From']
print 'Sub:', new_email_msg['Subject']
print 'Body:', new_email_msg.get_payload()


