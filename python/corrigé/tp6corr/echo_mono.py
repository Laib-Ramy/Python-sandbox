import socket

def echo_mono():
    host=''
    port=49631
    with socket.create_server((host, port)) as s:
        while True:
            conn, _ = s.accept()
            print("connected")
            with conn:
                while True:
                    data = conn.recv(1024)
                    received=data.decode("utf-8")
                    reply=f"echo: {received}".encode("utf-8")
                    if not data: break
                    conn.sendall(reply)


if __name__ == "__main__":
    echo_mono()