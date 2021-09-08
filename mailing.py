import smtplib
from email.message import EmailMessage

SUBJECT = '[Melisa Zulberti - website]'

def send_email(*args, **kwargs):
    email   = kwargs['email']
    name    = kwargs['name']
    message = kwargs['message']

    msg = EmailMessage()

    msg.set_content(message)

    msg['Subject'] = SUBJECT
    msg['From']    = email
    msg['To']      = 'matiaszulberti@gmail.com'

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("matiaszulberti@gmail.com", "########")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("[fatal-error] - {}".format(e))
        raise(e)
