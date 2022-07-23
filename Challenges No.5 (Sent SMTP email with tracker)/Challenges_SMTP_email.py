import email, smtplib, ssl 

from email import encoders 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = input("Type your gmail account and press enter: ")
gmail_password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = 'Testing Email sent via SMTP (With Attachment) - By Rick Poh'
message["From"] = gmail_user
message["To"] = 'ytbryan@gmail.com'

# Create the plain-text and HTML version of your message

email_text = """\
Hi Bryan, 
\n\n\nHow are you? 
\n\n\nRick Poh 
\nBest Regrads
"""
html = """\
<html>
  <body>
    <p>Hi, Bryan<br>
       How are you?<br>
       <a <img src="https://pastepixel.com/image/pQAPVVZb7VZYZtMyM4nN.png" alt=""/>  
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


filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part3 = MIMEBase("application", "octet-stream")
    part3.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part3)

# Add header as key/value pair to attachment part
part3.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part3)


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
    
