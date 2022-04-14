#!/usr/bin/python3
#
# This is a very simple SERVER implementation for a very very simple
# request/reply protocol.
#
import argparse
from importlib.resources import contents
from socket import *
import parser
import get
import put
import error


parser = argparse.ArgumentParser(description="Our HTTP Server.")
parser.add_argument('--port', dest='serverPort', type=int, default=8080,
                    help='Default listener port for the HTTP server')

args = parser.parse_args()



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', args.serverPort))
serverSocket.listen(1)

while True:
    print('Accepting connections')
    conn, addr = serverSocket.accept()
    print('Serving a connection from host', addr[0], 'on port', addr[1])
    request = conn.recv(1024)   # reading data (a request) from the connection
    if not request:
        print("empty message: bailing out!")
        break
    if request.decode('utf-8') == 'shutdown':
        print("shutdown request: bailing out!")
        break
    print('request:', request.decode('utf-8'))


    # Parse HTTP headers
    headers = request.decode('utf-8').split('\r\n')
    print(headers)
    method = headers[0].split()[0]
    print(method)
    filename = headers[0].split()[1]
    print(filename)
    protocol = headers[0].split()[2]
    print(protocol)
    host = headers[1].split()[1]
    print(host)
    host = host.split(":")[0]
    print(host)
    # Responses based on the HTTP Method
    # GET method
    if method == 'GET':
        response = get.get_files(filename, host, protocol)           
    # Method not allowed or not implemented
    
    #PUT method
    if method == 'PUT':
        content_type = headers[2].split()[1]
        body = (headers[3:])
        response = put.PUT_File(filename, host, protocol, content_type, body)
    
    #NTW22INFO
    if method == 'NTW22INFO':
        response = "Not implemented yet"
    
    else:
        response = error.error_handling(405)
        
    try:
        print(response)
        conn.sendall(response)
        
    finally:
        conn.close()

serverSocket.close()

