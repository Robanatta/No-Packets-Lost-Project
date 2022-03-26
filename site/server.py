#!/usr/bin/python3
#
# This is a very simple SERVER implementation for a very very simple
# request/reply protocol.
#
import socket
import sys



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

    # Da modificare la selezione di host e filename

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
            while i < len(vhosts):
                if vhosts[i] == host:
                    filename = '/' + vhosts[i + 1]
                i += 1

        try:
            # Get the content of the file
            fin = open(host + filename)
            content = fin.read()
            fin.close()

            response = 'HTTP/1.0 200 OK\n\n'
        except FileNotFoundError:

            response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
    # Method not allowed or not implemented
    else:
        response = 'HTTP/1.0 405 METHOD NOT ALLOWED\n\nMethod Not Allowed'

    
    print(response)
    conn.sendall(response.encode('utf-8'))
    conn.close()

s.close()

