from http import server
from pydoc import cli
from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        serversocket.bind(
            ("localhost", 9000)
        )  # here you use the IP address and port number as a tuple as arguments
        serversocket.listen(
            5
        )  # By using .listen(5), we can take upto 5 requests at a time, while executing one and sending the rest 4 to queue
        while True:
            (
                clientsocket,
                address,
            ) = (
                serversocket.accept()
            )  # This line accepts the request from the client/ browser, which is basically accepting the phone call

            rd = clientsocket.recv(
                5000
            ).decode()  # This is the counterpart of the .send() request from the client/ browser, here the server receives what the client is requesting in UTF-8 and decodes to Unicode for reading in python
            pieces = rd.split("\n")  # See doc string at the very end

            # So pieces[0] is the metadata and pieces[1] is the html script/ document

            if len(pieces[0]) > 0:
                # print(rd)
                print(pieces[0])  # Just printing the metadata/ headers

            data = "HTTP/1.1 200 OK\r\n"  # Adding response confirmation, if requested document is not found, there will be 404 not found
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"  # Adding the new line before the html script/ document
            data += "<html><body>Hello World!!</body></html>\r\n\r\n"  # the html script/ document that will be returned

            clientsocket.sendall(
                data.encode()
            )  # The data variable which is a string of response, will be encoded to UTF-8 and sent to the client/ browser now
            clientsocket.shutdown(
                SHUT_WR
            )  # After executing the request from a client, the server will move on to the next request in listen queue. Before moving, it will shut down the earlier request.

    except KeyboardInterrupt:
        print("\nShutting Down..\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()  # After sending the response, the socket will be hung up from the server side by this line

    # NOTE: the socket from the client side will also be shut down after getting the response


print("Access http://localhost:9000")
createServer()


# NOTE: This is what the server receives which is sent from the client side: We are printing only the first line by splitting the whole thing with \n as delimiter
"""
GET / HTTP/1.1
Host: localhost:9000
Connection: keep-alive
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7
"""
