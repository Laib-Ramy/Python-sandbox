import socket

host = 'localhost'  # The server's hostname or IP address
port = 49631        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        phrase=input("you: ")
        if phrase=='quit': 
            print("Bye!")
            break
        s.sendall(phrase.encode("utf-8"))
        data = s.recv(1024)
        print(data.decode('utf-8'))