import socket

def horloge_client():
    host='localhost'
    port=51793
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024)
        print(data.decode("utf-8"))

if __name__ == "__main__":
    horloge_client()