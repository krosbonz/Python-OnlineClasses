from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SASL, NTLM
import getpass

usr = input('What is your user name? ')
print(usr)
pswd = getpass.getpass('Password:')

# define the server and the connection
s = Server('lgh.local', get_info=ALL)
c = Connection(s, user="lgh\\"+ usr, password=""+ pswd, authentication=NTLM)
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)


