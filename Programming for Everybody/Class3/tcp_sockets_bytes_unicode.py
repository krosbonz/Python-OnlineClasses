#Python has built-in support for TCP Sockets

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#This prepares your system to make a connection
mysock.connect(('data.pre4e.org', 80))
#The connection location and port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#Get this website/page using HTTP followed by enter key twice (\n\n)
#.encode converts the string to bytes (UTF-8)
mysock.end

while True:
    data = mysock.recv(512)
    #Receive up to 512 characters (bytes)
    if (len(data) < 1):
        break
    #If the data length is less than 1 we know it is the end of file and the loop can end
    print(data.decode())
    #This is the opposite of .encode. It will convert the incoming UTF-8 data to unicode
mysock.close()
#Closes the connection

#When talk to external sources we send bytes
while True:
    data = mysock.recv(512)
    #This is in bytes (UTF-8)
    if (len(data)< 1):
        break
    mystring = data.decode()
    #When reading data from an external resource, the data must be decoded to Unicode so it can be represented in Python as a string
    print(mystring)

#Ordinals are the number equivalent to the 128 ASCII character map
print(ord('h'))
#Output
104