from socket import *

# we will use these to spefiy who to connect to
sName='localhost'
sPort=5012

# we are creating a client side socket artifiact
clientSock=socket(AF_INET,SOCK_DGRAM)

#create and send a message
message='Good Morning'
clientSock.sendto(message.encode(),(sName,sPort))

#expect and get a response from the server on the same socket
rmessage,rfrom=clientSock.recvfrom(1000)

#print what you received and close the connection
print(rmessage.decode())
clientSock.close()
