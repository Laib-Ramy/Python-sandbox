import socket
from datetime import datetime

def horloge():
    host=''
    port=51793
    with socket.create_server((host, port)) as s:
        while True:
            conn, _ = s.accept()
            with conn:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                conn.sendall(bytes(current_time+'\n', "utf-8"))

if __name__ == "__main__":
    horloge()