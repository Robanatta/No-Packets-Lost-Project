#!/usr/bin/python3
#
# This is a very simple SERVER implementation for a very very simple
# request/reply protocol.
#
import argparse
from importlib.resources import contents
from socket import *
#import parser
import get
import put
import delete
import error
import ntw22info


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
    request = conn.recv(2048)   # reading data (a request) from the connection
    if not request:
        print("empty message: bailing out!")
        break
    if request.decode('utf-8') == 'shutdown':
        print("shutdown request: bailing out!")
        break
    print('request:', request.decode('utf-8'))

    # Parser request
    try:
        request_splitted = request.decode('utf-8').split("\r\n")
        for i in request_splitted:
            if i.split(':')[0] == 'Host':
                request_host = i.split(':')[1][1:]
                break
        request_line = request_splitted[0]
        request_header = request_splitted[1:]
        request_method, request_resource, request_protocol = request_line.split(" ")
    except:
        response = error.error_handling(400, request_protocol) 

    if request_protocol != "HTTP/1.1" and request_protocol != "HTTP/1.0":
        response = error.error_handling(505, request_protocol) 
    else:
        # Responses based on the HTTP Method
        # GET method
        if request_method == 'GET':
            response = get.get_files(request_resource, request_host, request_protocol)      
        
        #DELETE method
        elif request_method == 'DELETE':
            response = delete.delete_files(request_resource, request_host, request_protocol)
        
        #PUT method
        elif request_method == 'PUT':
           content_type = request_header[2].split()[1]
        #    Content-Length = request_header[3].split()[1]
           body = (request_header[4:])
           response = put.PUT_File(request_resource, request_host, request_protocol, content_type, body)
        
        #NTW22INFO
        #elif request_method == 'NTW22INFO':
            #response = "Not implemented yet"
        
        else:
            response = error.error_handling(405, request_protocol)
    try:
        print(response)
        conn.sendall(response)
    finally:
        conn.close()

serverSocket.close()

