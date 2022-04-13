import os

def get_files(filename, host):
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
            response = ('HTTP/1.0 200 OK\n\n' + content).encode('utf-8')
        # In case it need files like png or gif            
        else:
            data = open(path, "rb")
            content = data.read()
            response = 'HTTP/1.0 200 OK\n\n'.encode('utf-8') + content

        data.close()

        
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found\n'.encode('utf-8')
    return response