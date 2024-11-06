from threading import Thread, Lock
import time

NUM_THREADS = 2

counter = 0
lock=Lock()

def racing_function():
    global counter
    global lock
    while True:
        with lock:
            counter += 1
            counter -= 1


def main():
    ts = [Thread(target=racing_function) for _ in range(NUM_THREADS)]
    for t in ts:
        t.daemon = True
        t.start()
    for i in range(30):
        print(counter)
        time.sleep(0.1)


main()
