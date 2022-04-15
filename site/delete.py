from aifc import Error
from http.client import SERVICE_UNAVAILABLE
import os
from datetime import datetime
import error 


def delete_files(filename, host, protocol):
    
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
            return(error.error_handling(404, protocol))


    
    path = os.path.join(host, filename[1:])
    name, extension = os.path.splitext(path)
    print(name)
    print(extension)
    try:
        if extension == ".html":
            request_content_type = "text/html"
        elif extension == ".txt":
            request_content_type = "text/plain"
        elif extension == ".jpeg":
            request_content_type = "image/jpeg"
        elif extension == ".png":
            request_content_type = "image/png" 
        else:
            request_content_type = "undefined" 

        os.remove(path)
        
        response_header = []
        response_status = " ".join([protocol, "200", "OK"])
        response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
        response_header.append(response_time)
        response_header.append("Server: Group NoPacketsLost Server")
        request_content_length = "Content-length: %s" % len(content) 
        response_header.append(request_content_length)
        response_header.append("Content-Type:" + request_content_type)  
        request_headers = "\r\n".join(response_header)

        response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')
        
        if extension == ".html" or extension == ".txt":
            content = content.encode('utf-8')
            
        response = response + content



    except FileNotFoundError:
        return(error.error_handling(404, protocol))
    except OSError:
        if type == 501:
            return(error.error_handling(501, protocol))
        if type == 503:
            return(error.error_handling(503, protocol))
