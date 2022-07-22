import email, smtplib, ssl #remove email if not able to run the program

from email import encoders #remove email if not able to run the program
from email.mime.base import MIMEBase #remove email if not able to run the program
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = input("Type your gmail account and press enter: ")
gmail_password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = 'Testing Email sent via SMTP (With Attachment) - By Rick Poh'
message["From"] = gmail_user
message["To"] = 'shizchaw95@gmail.com'

# Create the plain-text and HTML version of your message

email_text = """\
Hi Bryan, 
\n\n\nHow are you? 
Please refer to My GitHub Profile for my tech profile reference.
\n\nRick Poh 
\nBest Regrads
"""
html = """\
<html>
  <body>
    <p>Hi, Bryan<br>
       How are you?<br>
       Please refer to <a href="https://github.com/RickPoh95">My GitHub Profile</a> 
       for my tech profile reference.<br>
       Rick Poh<br>
       Best Regrads
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(email_text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Add body to email
message.attach(MIMEText(message["Subject"], "plain"))

filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

try:
    # Create a secure SSL context
    context = ssl.create_default_context()
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(message["From"], message["To"], message.as_string())
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
    
