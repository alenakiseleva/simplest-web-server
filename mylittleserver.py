#!/usr/bin/python
import sys
import socket
import os

port = int(sys.argv[1])
host_address = sys.argv[2]
serversocket = socket.socket()
serversocket.bind((host_address, port))
serversocket.listen(1)
while True:
	(clientsocket, address) = serversocket.accept()
	query = clientsocket.recv(2048)
	if not query:
		break
	query_strings = query.split()
	print query_strings
	print 'hey'
	if query_strings[0] == 'GET':
		print 'get'
		filePath = os.getcwd() + query_strings[1]
		if os.path.isdir(filePath):
			if filePath[-1] != '/':
				filePath = filePath + '/'
			filePath = filePath + 'index.html'
		print filePath
		fileExists = os.path.exists(filePath)
		print fileExists
		if fileExists:
			requestedFile = open(filePath)
			answer = '''HTTP/1.1 200 Ok

			''' + requestedFile.read()
			print answer
			clientsocket.send(answer)
		else:
			page404 = open(os.getcwd() + '/404.html')
			answer = '''HTTP/1.1 404 Not found

			''' + page404.read()
			print answer
			clientsocket.send(answer)	
	else:
		print 'not get'
	clientsocket.close()
print 'Close server work'	
serversocket.close()
