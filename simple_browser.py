import socket

# create a socket in your local machine
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make the phone call to a domain name and a port in that domain name
mysock.connect(("data.pr4e.org", 80))

# send the command
cmd = (
    "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
)  # encode it to convert the Python Unicode string to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    print(
        data.decode(), end=""
    )  # The data that comes in, is in UTF-8, but python prints in Unicode, so it UTF-8 is decoded first and converted to Unicode for Python to print

mysock.close()
