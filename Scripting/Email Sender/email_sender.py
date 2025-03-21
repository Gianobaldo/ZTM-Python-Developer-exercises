import smtplib #allows us to sned the email by creating a server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Gianfranco Obaldo'
email['to'] = 'bopayo4096@isorax.com'
email['subject'] = 'Dont forget to complete your purchase'

email.set_content(html.substitute({'name' :"Luffy'"}), 'html')

with smtplib.SMTP(host= "smtp.gmail.com", port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls() #encription to connect securely to server
	smtp.login('email@gmail.com''123456')
	smtp.send_message(email)
	print("all good boss")
