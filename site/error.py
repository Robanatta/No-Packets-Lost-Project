from datetime import datetime

def error_handling(type, protocol):
    response_header = []
    # Based on the number of the error creates the correct response to send
    if type == 400:
        response_status = " ".join([protocol, "400", "BAD REQUEST"])
    elif type == 403:
        response_status = " ".join([protocol, "403", "FORBIDDEN"])
    elif type == 404:
        response_status = " ".join([protocol, "404", "FILE NOT FOUND"])
    elif type == 405:
        response_status = " ".join([protocol, "405", "METHOD NOT ALLOWED"])
    elif type == 501:
        response_status = " ".join([protocol, "501", "NOT IMPELMENTED"])
    elif type == 505:
        response_status = " ".join([protocol, "505", "HTTP VERSION NOT SUPPORTED"])
    else:
        response_status = " ".join([protocol, "500", "INTERNAL SERVER ERROR"])

    response_time = datetime.today().strftime('%a, %d %b %Y %X %Z')
    response_header.append(response_time)
    response_header.append("Server: Group NoPacketsLost Server")
    request_headers = "\r\n".join(response_header)

    response = (response_status + "\r\n" + request_headers + "\r\n\r\n").encode('utf-8')
    return response
