#!/usr/bin/python3
#
# This is a very simple SERVER implementation for a very very simple
# request/reply protocol.
#
from asyncio.windows_events import NULL
from importlib.resources import contents
import socket
import sys
from email.policy import default
import socket
import os
import argparse
import datetime




if len(sys.argv) > 1:
    port_number = int(sys.argv[1])
else:
    port_number = 1234




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', port_number))
s.listen(1)

while True:
    print('Accepting connections')
    conn, addr = s.accept()
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
    headers = request.decode('utf-8').split('\n')
    method = headers[0].split()[0]
    filename = headers[0].split()[1]
    host = headers[1].split()[1]

    

    # Responses based on the HTTP Method
    # GET method
    if method == 'GET':

        # In case of '/' we get entry_point_file from the vhosts.conf file
        if filename == '/':
            # Open vhosts.conf file
            vin = open('vhosts.conf')
            vhosts = vin.read()
            vin.close()
            vhosts = vhosts.split(",")

            i = 0
            print(vhosts)
            while i < len(vhosts):
                if vhosts[i] == host:
                    filename = '/' + vhosts[i + 1]
                    break
                i += 1

        try:
            # Get the content of the file
            # In case it need the html page
            if filename.endswith('.html'):
                data = open(host + filename, "r")
                content = data.read()
                response = ('HTTP/1.0 200 OK\n\n' + content).encode('utf-8')
            # In case it need files like png or gif            
            else:
                data = open(host + filename, "rb")
                content = data.read()
                response = 'HTTP/1.0 200 OK\n\n'.encode('utf-8') + content

            data.close()

            
        except FileNotFoundError:

            response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found\n'.encode('utf-8')



    #PUT METHOD
    if method == 'PUT':
        conn.close()
            
    # Method not allowed or not implemented
    else:
        response = 'HTTP/1.0 405 METHOD NOT ALLOWED\n\nMethod Not Allowed\n'.encode('utf-8')

    print(response)
    try:
        conn.sendall(response)
        
    finally:
        conn.close()

s.close()

