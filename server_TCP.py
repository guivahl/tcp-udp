from socket import *

def messageService (message):
	headerLength = 3 # length of 'CA:' and 'CB:' keys

	if message.startswith("CA:"):
		payload = message[headerLength:]
		return payload.lower()

	if message.startswith("CB:"):
		payload = message[headerLength:]
		return payload.upper()
	
	return message

serverIP = 'localhost'  # localhost or your server IP address
serverPort = 9999		# use the port number you wish (higher than 1023)

serverSocket = socket(AF_INET,SOCK_STREAM)	# creates a socket (server side)
serverSocket.bind((serverIP, serverPort))	# bind() associates the socket with its local address [bind() is used in the server side]

serverSocket.listen(1)

print("Server {} running on port {}!".format(serverIP, serverPort))

while 1:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1500)		# 1500 bytes are read from the socket
    decodedMessage = message.decode()

    print("Mensagem recebida: " + decodedMessage)
	
    responseMessage = messageService(decodedMessage)
    
    encodedMessage = responseMessage.encode()

    connectionSocket.send(encodedMessage)		# sends converted (upper-case) sentence
    connectionSocket.close()
