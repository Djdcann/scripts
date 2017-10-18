import time
import imaplib
import email

def send_email(user, pwd, recipient, subject, body):
    import smtplib
    
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        #server.ehlo()
        #server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print e.message
        print "failed to send mail"

        
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "super" + ORG_EMAIL
FROM_PWD    = "secret"
SMTP_SERVER = "imap.gmail.com"

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)#port 993
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('Bandcamp')
        #mail.create('godlike')
        print mail.list()
        typ, data = mail.search(None, '(SUBJECT "new alhambra")')
        mail_ids = data[0].split()
        print mail_ids

        #id_list = mail_ids.split()
        #first_email_id = int(id_list[0])
        #latest_email_id = int(id_list[-1])

        for i in xrange(3, 0, -1):
            typ, data = mail.fetch(i, '(RFC822)')
            print typ

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    if msg.is_multipart():
                        for payload in msg.walk():
                            # if payload.is_multipart(): ...
                            print payload.get_content_type()
                            if payload.get_content_type() == 'text/plain':
                                print payload.get_payload(decode=True)
                    else:
                        print msg.get_payload(decode=True)
                else:
                    print 'wow'

    except Exception, e:
        print str(e)


if __name__ == '__main__':
    read_email_from_gmail()
