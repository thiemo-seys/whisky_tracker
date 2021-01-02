from smtplib import SMTP_SSL, SMTPHeloError, SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError, \
    SMTPNotSupportedError
from ssl import create_default_context

#TODO: make a gmail address for this program, find a way to store the password,email securely(maybe in config file, although that is tricky with uploading the project to Github)


def sendmail(sender_email, password, receiver_emails, message, port=465):
    try:
        context = create_default_context()
        with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("my@gmail.com", password)
            return server.sendmail(sender_email, receiver_emails, message)
    except SMTPHeloError as e:
        pass
    except SMTPRecipientsRefused as e:
        pass
    except SMTPSenderRefused as e:
        pass
    except SMTPDataError as e:
        pass
    except SMTPNotSupportedError as e:
        pass
    except Exception as e:
        print(e)
