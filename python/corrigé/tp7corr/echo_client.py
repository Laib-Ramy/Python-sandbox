import socket


def main():
    port=49631
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', port))
    request = None

    while request != 'quit':
        request = input('you: ')
        if request:
            server.send(request.encode('utf8'))
            response = server.recv(255).decode('utf8')
            print(response)


if __name__ == "__main__":
    main()
