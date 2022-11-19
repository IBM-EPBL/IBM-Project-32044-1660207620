import sendgrid as SendGridAPIClient
import smtplib 
server  = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "expense tracker"
def sendgridmail(user,TEXT):
    from_email = Email("bowmithachandrasekaran@gmail.com") 
    to_emails = To(user) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    
    mail = Mail(from_email, to_emails, subject, content)

    # Get a JSON-ready representation of the Mail object
    
    # Send an HTTP POST request to /mail/send
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.headers)
    except Exception as e:
        print(e)
sendgridmail("aswin28800@gmail.com","this is test mail")
server.login('bowmithachandrasekaran@gmail.com',"ntofulqqooyroxxi")
server.sendmail("bowmithachandrasekaran@gmail.com","aswin28800@gmail.com","this is test mail")








