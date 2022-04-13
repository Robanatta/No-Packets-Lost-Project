import os
from datetime import datetime
import error 


def get_files(filename, host, protocol):
    
    # In case of '/' we get entry_point_file from the vhosts.conf file
    if filename == '/':
        # Open vhosts.conf file
        vin = open('vhosts.conf')
        vhosts = vin.readline()
        while vhosts:
            vhosts = vhosts.split(",")
            if vhosts[0] == host:
                filename = '/' + vhosts[1]                
            vhosts = vin.readline()
        vin.close()
        if filename == '/':
            return(error.error_handling(404))


    
    path = os.path.join(host, filename[1:])
    name, extension = os.path.splitext(path)
    try:
    

        if extension == ".html":
            request_content_type = "text/html"
            data = open(path, "r")
        elif extension == ".txt":
            request_content_type = "text/plain"
            data = open(path, "r")
        elif extension == ".jpeg":
            request_content_type = "image/jpeg"
            data = open(path, "rb")
        elif extension == ".png":
            request_content_type = "image/png" 
            data = open(path, "rb")
        else:
            request_content_type = "undefined" 
            data = open(path, "rb")
            

        content = data.read()

        response_header = []
        response_status = " ".join([protocol, "200", "OK"])
        response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
        response_header.append(response_time)
        response_header.append("Server: Group NoPacketsLost Server")
        request_content_length = "Content-length: %s" % len(content) 
        response_header.append(request_content_length)
        response_header.append(request_content_type)  
        request_headers = "\r\n".join(response_header)

        response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')
        
        if extension == ".html" or extension == ".txt":
            content = content.encode('utf-8')
            
        response = response + content

        data.close()

        
    except FileNotFoundError:
        return(error.error_handling(404))

    return response