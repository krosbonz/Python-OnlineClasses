import imapclient
import datetime
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
email = input("Email address for authenticating: ")
pw = input("Password for email account: ")
imapObj.login(f'{email}', f'{pw}')

inbox = imapObj.select_folder('INBOX', readonly=True)
# Selects the email folder and sets it so the work we do will be read only
# "Inbox" is most often used, but not the only option. To generate a list: object.list_folders
UIDs = imapObj.search([u'SINCE', datetime.date(2019, 1, 1)])
# Find emails. In this case it will find all emails since Jan 1 2019
# This returns a list of unique IDs
print(UIDs)

for UID in UIDs:
    rawMessages = imapObj.fetch([UID], ['BODY[]', 'FLAGS'])
    # This fetches the body and various flags of the specified message
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
    # PyzMessage.factory parses the raw information from ".fetch"
    if message.text_part != None:
        txtmsg = message.text_part.get_payload().decode(message.text_part.charset)
        print(txtmsg)
    else:
        htmlmsg = message.html_part.get_payload().decode(message.html_part.charset)
        print(htmlmsg)
    # If the email contains plain text print it, otherwise print the html
    # The ".decode" can generally be set to "UTF-8", but "message.html_par.charset" will try to decifer the format type

    # There are a few bits of info we can get from Pyzmail without printing ALL of the email info from above
    # message.get_subject()
    # message.get_addresses('from')
    # message.get_address('to')

# Information on IMAPClient and pyzmail;
# https://imapclient.readthedocs.org
# https://magiksys.net/pyzmail
# https://automatetheboringstuff.com/chapter16/
