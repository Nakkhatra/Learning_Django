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
            pieces = rd.split(
                "\n"
            )  # As the format of the response usually contains metadata (containing headers) at the beginning, then a new line and then the html script/ document: So we are splitting the first part (metadata) and the html script or document into two pieces by using delimiter "\n"

            # So pieces[0] is the metadata and pieces[1] is the html script/ document

            if len(pieces[0]) > 0:
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
