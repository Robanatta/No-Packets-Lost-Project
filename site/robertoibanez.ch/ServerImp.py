#MATIAS IMPLEMENTATION
# Tests
#curl RobertoIbanez.ch:8080/
#telnet
#
# 200,
# 201 = SUccesfully created put request
# ,400,403,404,405,501,505

#GET / HTTP/1.1
#Host: robertoibanez.ch:8080
#Connection: keep-alive
#Cache-Control: max-age=0
#Upgrade-Insecure-Requests: 1





import argparse
import os
from socket import *

parser = argparse.ArgumentParser(description="HTTP 1/0 Server.")
parser.add_argument('--port', dest='serverPort',type=int, default=8080,
    help='Default listener port for HTTP 1/0 server')

args = parser.parse_args()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', args.serverPort))
serverSocket.listen(1)

while(True):
    print("Listening for connections")
    connectionSocket, addr = serverSocket.accept()
    print("Connection Established")
    request = connectionSocket.recv(2048).decode()
    print(request)
    request_split = request.split("\r\n")
    request_line = request_split[0]
    #this is a semplification, we have to consider when we get \r and \n
    #the request can also have a body if is a put method
    #First we have to know what method it is
    request_header = request_split[1:]

    # handle get method
    request_method, request_resource, request_protocol = request_line.split(" ")
    if (request_method == 'GET'):
        print("I got a GET")
        request_resource_path = os.path.join(request_resource[1:])
        print(request_resource)
        print(request_resource_path)
        os.path.exists()


    elif(request_method == 'PUT'):
        print("I got a PUT")


    elif(request_method == 'DELETE'):
        print("I got a DELETE")

        
    else:
        print("Error code needed: an error occurried")
    #elif(request_method == '')



