#PUT implementation

# Syntax: PUT /new.html HTTP/1.1

#Example of request:
#    PUT /new.html HTTP/1.1
#   Host: robertoibanez.ch
#   Content-type: text/html
#   Content-Length: 16
#   
#
#   <p>New File</p>

#Example of response:
#   HTTP/1.1 201 Created
#   Content-Location: /new.html

import os
import error

def PUT_File(filename, host,protocol, content_type, body):
    # In case of '/' we get entry_point_file from the vhosts.conf file
    if filename == '/':
        # Open vhosts.conf file
        vin = open('vhosts.conf')
        vhosts = vin.readline()
        # Search for the host in the file vhost.conf
        while vhosts:
            vhosts = vhosts.split(",")
            if vhosts[0] == host:
                filename = '/' + vhosts[1]                
            vhosts = vin.readline()
        vin.close()
        # If it didn't found it then it means that host is not supported
        if filename == '/':
            return(error.error_handling(404, protocol))

    #path = os.path.join(host, filename[1:])
    #path = ("/" + path)
    path = os.path.join("/",filename[1:])
    #if os.path.exists():
    name, extension = os.path.splitext(path)

    if extension == ".html":
        request_content_type = "text/html"
        data = open(path, "w")
        for i in range(0, len(body)):
            data.write(body[i])
        data.close()
    elif extension == ".txt":
        request_content_type = "text/plain"
        data = open(path, "w")
        for i in range(0, len(body)):
            data.write(body[i])
        data.close()
    elif extension == ".jpeg":
        request_content_type = "image/jpeg"
        data = open(path, "wb")
        for i in range(0, len(body)):
            data.write(body[i])
        data.close()
    elif extension == ".png":
        request_content_type = "image/png" 
        data = open(path, "wb")
        for i in range(0, len(body)):
            data.write(body[i])
        data.close()
    else:
        request_content_type = "Type Not supported" 
        
    response_header = []
    response_status = " ".join([protocol, "201", "Created"])
    response_location = " ".join(["Content-Location:", path] )
    response_header.append(response_location)
      
    request_headers = "\r\n".join(response_header)

    response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')

    return response

    
