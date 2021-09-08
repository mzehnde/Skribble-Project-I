import os
from email.mime.application import MIMEApplication
from flask import Flask
from flask_restful import Api
from pip._vendor import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__)
api = Api(app)


class Email:
    def __init__(self, receiverEmail, response, username, fileName):
        self.receiverEmail = receiverEmail
        self.response = response
        self.username = username
        self.fileName = fileName

    def sendEmail(self):
        body = '''Dear ''' + self.username + ''', attached you will find your signed PDF File'''
        sender = 'max.zehnder@skribble.com'
        password = 'loidmyzngwkpddzk'
        receiver = self.receiverEmail
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'Signed PDF'
        message.attach(MIMEText(body, 'plain'))
        attach = MIMEApplication(self.response.content, _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename=self.fileName)
        message.attach(attach)
        # use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        # enable security
        session.starttls()

        # login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')


@app.route('/success/<string:document_id>/<string:token>/<string:receiverEmail>/<string:username>/<string:fileName>', methods=['POST'])
def sendEmail(document_id, token, receiverEmail, username, fileName):
    header = {'Authorization': 'Bearer' + token}
    response = requests.get('https://api.scribital.com/v1/documents/' + document_id + '/content',
                            headers=header)
    email = Email(receiverEmail, response, username, fileName)
    email.sendEmail()
    return "Email has been sent"


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
