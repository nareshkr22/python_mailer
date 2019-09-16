import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders  
me = "me@gmail.com" 
msg = MIMEMultipart('alternative')
msg['From'] = me
#to send attachment
filename=r'name_of_file'
attachment = open(r"path_of_file", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)

emails = ['me@gmail.com','you@gmail.com']
for mail_id in emails: 
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    msg['Subject'] = "Custom Subject Line"
    mail.login('username', 'password')
    msg['To'] = mail_id
    # Create the body of the message (a plain-text and an HTML version).
    html = """\
    <p>Dear """+ mail_id+ """</p>
    How are you

    """

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail.sendmail(me,mail_id, msg.as_string())
    mail.quit()
