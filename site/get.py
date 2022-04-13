import os
from datetime import datetime
import magic


def get_files(filename, host, protocol):
    
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
                break
            i += 1
    path = os.path.join(host, filename[1:])
    print(path)
    try:
        # Get the content of the file
        # In case it need the html page
        if filename.endswith('.html'):
            data = open(path, "r")

            content = data.read()

            response_header = []
            response_status = " ".join([protocol, "200", "OK"])

            response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
            response_header.append(response_time)
            response_header.append("Server: Group NoPacketsLost Server")
            request_content_length = "Content-length: %s" % len(content) 
            response_header.append(request_content_length)
            request_headers = "\r\n".join(response_header)



            response = (response_status + "\r\n" + request_headers + "\r\n\r\n"+ content).encode('utf-8')
        # In case it need files like png or gif            
        else:
            data = open(path, "rb")
            content = data.read()
            response_status = " ".join([protocol, "200", "OK"])
            response_header = []
            request_content_length = "Content-length: %s" % len(content) 
            response_header.append(request_content_length)
            request_headers = "\r\n".join(response_header)


            response = (response_status + "\r\n" + response_header + "\r\n\r\n"+ content).encode('utf-8')

        data.close()

        
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND File Not Found'.encode('utf-8')
    print(response)
    return response