import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
# SMTP server
conn.ehlo()
# Start the connection
conn.starttls()
# Allows user name to be encrypted 
email = input("Enter your Gmail email address for authentication: ")
pw = input("Enter your Gmail password (it will be sent encrypted): ")
conn.login(email, pw)
# Email address and password for authentication to Gmail SMTP
recip = input("Email address of recipient: ")
subj = input("Enter subject of email: ")
body = input("Enter the body of your email: ")
conn.sendmail(email, recip, f'Subject: {subj} \n\n {body}')
# Email from and to address
# First new line character ends the "Subject" and the second new line char ends the header section
{}
# Required position for the script to put failed email notifications
conn.quit

