
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SASL, NTLM

# define the server and the connection
server = Server('www.zflexldap.com', get_info=ALL)
conn = Connection(server, 'cn=ro_admin,ou=sysadmins,dc=zflexsoftware,dc=com', 'zflexpass', auto_bind=True)
conn.search('dc=zflexsoftware,dc=com', '(objectclass=computer)')

conn.entries