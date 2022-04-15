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
            return(error.error_handling(404))


    
    path = os.path.join(host, filename[1:])
    name, extension = os.path.splitext(path)
    print(name)
    print(extension)
    try:
    
        os.remove(path)

    except FileNotFoundError:
        return(error.error_handling(404, protocol))
    except OSError:
        if type == 501:
            return(error.error_handling(501, protocol))
        if type == 503:
            return(error.error_handling(503, protocol))
