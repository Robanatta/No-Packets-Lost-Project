def error_handling(type):
    if type == 404:
        return 'HTTP/1.0 404 NOT FOUND File Not Found'.encode('utf-8')
    elif type == 405:
        return 'HTTP/1.0 405 METHOD NOT ALLOWED\n\nMethod Not Allowed\n'.encode('utf-8')
    else:
        return 'HTTP/1.0 501 NOT IMPLEMENTED Not implemented'.encode('utf-8')