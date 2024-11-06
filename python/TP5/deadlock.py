from threading import Thread, Lock
import time


class RoadLane(Thread):
    def __init__(self, name, delta_t=0.1):
        Thread.__init__(self)
        self.name = name
        self.delta_t = delta_t
        self.counter = 0
        self.right_priority = None
        self.engaging = Lock()

    def run(self):
        while True:
            if self.right_priority:
                with self.right_priority:
                    with self.engaging:
                        print(f"{self.name}:{self.counter}")
                        self.counter += 1
            time.sleep(self.delta_t)


def model_crossroad():
    pass


model_crossroad()
