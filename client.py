Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

import sys
import socket
import pickle
import threading
from threading import Thread

class Client():

	def __init__(self):
		
		# create a socket object
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# get local machine name
		host = socket.gethostname()
		
		port = 6666
		
		# bind to the port
		self.sock.connect((host, port))
		
		receive_message = Thread(target = self.receiveMessage)

		receive_message.daemon = True
		receive_message.start()

		while True:
                        message = raw_input('')

                        # pickle is used for object data serialization
                        self.sock.send(pickle.dumps(username + ": " + message))
				
	def receiveMessage(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass
		
username = raw_input("Choose an username:")
	
client = Client()

