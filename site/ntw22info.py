import email
import os
from datetime import datetime
import error
def NTW22INFO_method(protocol, host):
   
    try:
        filename = ''
        # Open vhosts.conf file
        vin = open('vhosts.conf')
        vhosts = vin.readline()
        # Search for the host in the file vhost.conf
        while vhosts:
            vhosts = vhosts.split(",")
            if vhosts[0] == host:
                filename = '/' + vhosts[1] 
                propname = vhosts[2] 
                email = vhosts[3] 
                break               
            vhosts = vin.readline()
        vin.close()
        # If it didn't found it then it means that host is not supported
        if filename == '':
            return(error.error_handling(404, protocol))


        
        path = os.path.join(host, filename[1:])
        name, extension = os.path.splitext(path)
        # Based on the extension the request and the data type to open changes
        if extension == ".html":
            request_content_type = "text/html"
            data = open(path, "r")
        elif extension == ".txt":
            request_content_type = "text/plain"
            data = open(path, "r")
        else:
            request_content_type = "undefined" 
            data = open(path, "rb")
            

        content = data.read()

        # Creates the response to send
        response_header = []
        response_status = " ".join([protocol, "200", "OK"])
        response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
        response_header.append(response_time)
        response_header.append("Server: Group NoPacketsLost Server")
        request_content_length = "Content-length: %s" % len(content) 
        response_header.append(request_content_length)
        response_header.append("Content-Type:" + request_content_type)  
        request_headers = "\r\n".join(response_header)
        request_text = "The administrator of " + host + " is " + propname + "\r\n" + "You can conctat him at " + email
        

        response = (response_status + "\r\n" + request_headers + "\r\n\r\n" + request_text).encode('utf-8')
            
        data.close()
        return response

    except FileNotFoundError:
        return(error.error_handling(404, protocol))
    except OSError:
        if type == 501:
            return(error.error_handling(501, protocol))
        if type == 503:
            return(error.error_handling(503, protocol))

    
    