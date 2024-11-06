from threading import Thread,Lock
import time

NUM_THREADS = 120

counter = 0

lock=Lock()
def racing_function():
    global counter
    while True:
        lock.acquire()
        try:
            counter += 1
            counter-=1
        finally:
            # Always release the lock
            lock.release()
        time.sleep(0.001)
        
def main():
    ts = [Thread(target=racing_function) for _ in range(NUM_THREADS)]
    for t in ts:
        t.daemon = True
        t.start()
    for i in range(30):
        print(counter)
        time.sleep(0.1)


main()
