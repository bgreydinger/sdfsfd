import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(name, email, job):
    try:
        MY_ADDRESS = app.config['MAIL_ADDRESS']
        PASSWORD = app.config['MAIL_PASSWORD']
    except:
        MY_ADDRESS = 'coronaconnectapp@gmail.com'
        PASSWORD = 'vrszlozolxagziwl'

    if job == "delivery":
        message = 'messagedel.txt'
    else:
        message = 'messagereq.txt'

    with open("main/messagetemplates/" + message, 'r', encoding='utf-8') as template_file:
        message_template = Template(template_file.read())

    # set up the SMTP server
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name)

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="CORONAHELP"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
