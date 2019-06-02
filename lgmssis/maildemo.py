
import os
import smtplib
from email.message import EmailMessage


EMAIL_ADDRESS = ('shazflicks@gmail.com')
EMAIL_PASSWORD = ('ILOVECHOBE25')
#i will set this once I edited the .bash profile
# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Application Received'
msg['From'] = EMAIL_ADDRESS
msg['To'] = '42force@gmail.com'
msg.set_content('Thank you for your Application')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h2 class="h2">This is an HTML EMAIL!</h2>
    </body>
</html>""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
