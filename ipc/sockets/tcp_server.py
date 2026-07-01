from socket import *
serverName = ''
serverPort = 1053

# create server side socket
serverSocket = socket(AF_INET,SOCK_STREAM)

# allow connections on a specific port and IP address
serverSocket.bind((serverName,serverPort))

# wait for connections
serverSocket.listen(1)
print('The server is ready to receive')

# repeatedly get connections from clients
while True:
     # wait and accept a connection from a client
     # Note: This also created a new "connection specific socket"
     connectionSocket, addr = serverSocket.accept()
     
     # on that connection specific socket receive some data
     sentence = connectionSocket.recv(1024).decode()

     # modify and create a new data
     capitalizedSentence = sentence.upper()

     #send that modified data
     connectionSocket.send(capitalizedSentence.encode())
     
     print('R: '+sentence)
     print('S: '+capitalizedSentence)

     #close the connection specific socket
     connectionSocket.close()

