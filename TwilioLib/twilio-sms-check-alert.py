import twilio
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


from twilio.rest import Client
from datetime import datetime


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

strFrom = 'reporting@baaz.com'
strTo = 'devops.theqar@baaz.com,majdi.kaaniche@baaz.com'
msg = MIMEMultipart()
msg['From'] = 'reporting@baaz.com'
msg['To'] = 'majd.jamaah@baaz.com'
msg['Subject'] = "Twilio SMS Alert !!"


# getting current date and time
d = datetime.today()

# getting current year

#getting current month

#getting current day

account_sid = 'XXXX' #NEED TO BE CHANGED!
auth_token =  'XXXX' #NEED TO BE CHANGED!
client = Client(account_sid, auth_token)

yesterday=d.day-1
messages = client.messages.list(date_sent=datetime(d.year, d.month, yesterday, 0, 0, 0))
SmsNumber=len(messages)


if SmsNumber >= 750:
	body = "Twilio SMS sent for Yesterday %d-%d-%d is %d " % (d.year,d.month,yesterday,SmsNumber)
	msg.attach(MIMEText(body, 'plain'))
	text=msg.as_string()
	server = smtplib.SMTP('smtp.office365.com', 587)
	server.ehlo()
	server.starttls()
	server.login('reporting@baaz.com','$tghfg2657hghHD@*#JSK')
	server.sendmail(strFrom, strTo.split(","), text)
	server.quit()
