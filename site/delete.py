import os
from datetime import datetime
import error 


def delete_files(filename, host, protocol):

    try:
        path = ""
        #delete only if host really exist in our virtual server
        vin = open('vhosts.conf')   
        vhosts = vin.readline()
        while vhosts:
            vhosts = vhosts.split(",")
            if vhosts[0] == host:
                path = os.path.join(host, filename[1:]) 
                os.remove(path)
                break              
            vhosts = vin.readline()
        if path == "":
            return(error.error_handling(404, protocol))
        
        
        response_header = []
        response_status = " ".join([protocol, "200", "OK"])
        response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
        response_header.append(response_time)
        response_header.append("Server: Group NoPacketsLost Server")
        request_headers = "\r\n".join(response_header)

        response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')
        
        return response



    except FileNotFoundError:
        return(error.error_handling(404, protocol))
    except OSError:
        if type == 501:
            return(error.error_handling(501, protocol))
        if type == 503:
            return(error.error_handling(503, protocol))
