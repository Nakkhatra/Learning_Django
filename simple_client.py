import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(
        ("127.0.0.1", 9000)
    )  ## 127.0.0.1 is the ipv4 for loopback right to the host/ localhost ip address

    cmd = (
        "GET http://127.0.0.1/sample.txt HTTP/1.0\r\n\r\n".encode()
    )  # Question: http://127.0.0.1/sample.txt actually contains nothing, but still how is the request a valid one and working????
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

except ConnectionRefusedError:
    print(
        "!!!Connection refused. Please check if server is running and accepting requests!!!"
    )

mysock.close()
