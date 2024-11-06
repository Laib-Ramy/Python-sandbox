from threading import Thread, Event
from random import randrange


class TabMul(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.working = True      # A flag set in the main thread to stop the secondary
        self.answered = Event()  # An event to signal that the answer is there
        self.answer = 0          # The answer
        self.count = 0           # The question counter
        self.count_correct = 0   # The counter of correct answers

    def run(self):
        while True:
            a = randrange(2, 10)
            b = randrange(2, 10)
            print(f'{a} x {b} = ')
            self.answered.clear()
            self.answered.wait(5)
            if not self.working:
                break
            self.count += 1
            if not self.answered.is_set():
                print("Too late!")
            else:
                try:
                    n = int(self.answer)
                    if n == a*b:
                        print('OK')
                        self.count_correct += 1
                    else:
                        print('Nope!')
                except(ValueError):
                    print("Not an integer")


def main():
    t = TabMul()
    t.start()
    while True:
        s = input()
        if s == 'quit':
            t.working = False
            t.answered.set()
            t.join()
            print(f"{t.count_correct} out of {t.count} correct answers. Bye!")
            break
        t.answer = s
        t.answered.set()


main()
