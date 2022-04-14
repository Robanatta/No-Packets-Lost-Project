import os
from datetime import datetime
import error
def NTW22INFO_method(protocol, host):
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
    
    