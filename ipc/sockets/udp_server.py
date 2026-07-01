from socket import *

# The port on which server will accept a client request
sName=''
sPort=5012

# create the socket for the server side
srvrSock=socket(AF_INET,SOCK_DGRAM)

# now set the IP and port number to accept messages
srvrSock.bind((sName,sPort))
print('Server is ready')

# do this forever
while True:
    # accept a message from the client
    rmessage,client=srvrSock.recvfrom(1000)

    # modifiy the message
    smessage=rmessage.decode().upper()

    #send the modified message as a response
    srvrSock.sendto(smessage.encode(),client)
