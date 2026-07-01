from socket import *
serverName = 'iiitb.ac.in'

# port to send to 80 or something like 61591
serverPort = 61591

# some possible messages to send
sentence='How are you?'
http_get='GET / HTTP/1.1\r\nHost: iiitb.ac.in\r\n\r\n'
msg=http_get

# create a client side socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Use that socket to make a connection to the server process
clientSocket.connect((serverName,serverPort))

# read a sentance and send it to the connected server process
#sentence = input('Input lowercase sentence:')
#clientSocket.send(sentence.encode())

clientSocket.send(msg.encode())

# expect and receive a sentance from the server process on the same socket
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())

# close the socket
clientSocket.close()
