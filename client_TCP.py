from socket import *

serverIP = 'localhost'  # localhost or your server IP address
serverPort = 9999		# use the port number you wish (higher than 1023)

clientSocket = socket(AF_INET, SOCK_STREAM)  # creates a socket (client side)
clientSocket.connect((serverIP, serverPort))

message = input('Enter your lower-case word: ')

encodedMessage = message.encode()

clientSocket.send(encodedMessage)     # sends the message to server 

modifiedMessage = clientSocket.recv(1500)         # 1500 bytes are read from the socket
decodedMessage = modifiedMessage.decode()

print(decodedMessage)   # print received/decoded message

clientSocket.close()