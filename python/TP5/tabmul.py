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
        # complétez le code
        pass


def main():
    t = TabMul()
    t.start()
    # complétez le code
    pass


main()
