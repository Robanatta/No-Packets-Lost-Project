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

def PUT_File(filename, host,protocol, content_type, body):
    path = os.path.join(host, filename[1:])
    #if os.path.exists():
    name, extension = os.path.splitext(path)
    if extension == ".html":
        request_content_type = "text/html"
        data = open(path, "w")
        data.write(body)
        data.close()
    elif extension == ".txt":
        request_content_type = "text/plain"
        data = open(path, "w")
        data.write(body)
        data.close()
    elif extension == ".jpeg":
        request_content_type = "image/jpeg"
        data = open(path, "wb")
        data.write(body)
        data.close()
    elif extension == ".png":
        request_content_type = "image/png" 
        data = open(path, "wb")
        data.write(body)
        data.close()
    else:
        request_content_type = "Type Not supported" 
        
    response_header = []
    response_status = " ".join([protocol, "201", "Created"])
    response_location = " ".join(["Content-Location:", filename] )
    response_header.append(response_location)
      
    request_headers = "\r\n".join(response_header)

    response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')

    return response

    
