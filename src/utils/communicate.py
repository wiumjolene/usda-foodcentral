import smtplib
from dotenv import find_dotenv, load_dotenv
from src.utils import config
import pymsteams
import os

class Communication:

    def email(msg, subject):
        FROM = 'NOTIFICATIONS!'
        user = 'notificationsforsumitins@gmail.com'
        TO = ''
        pwd = ''
        SUBJECT = subject
        TEXT = msg

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print ('successfully sent the mail')
        except:
            print( "failed to send mail")

        return()

    def teams(self, title, message):
        load_dotenv(find_dotenv())
        WEBHOOK = os.environ.get('TEAMSWEBHOOK')
        myTeamsMessage = pymsteams.connectorcard(WEBHOOK)
        myTeamsMessage.title(title)
        myTeamsMessage.text(message)
        myTeamsMessage.send()

        return