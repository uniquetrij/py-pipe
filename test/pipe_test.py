import random
from threading import Thread
from time import sleep

from py_pipe.pipe import Pipe

pipe = Pipe()


def generator():
    while True:
        pipe.push_wait()
        pipe.push(random.randrange(-10, 10))
        sleep(1)


def cumulative_adder():
    sum = 0
    while True:
        pipe.pull_wait()
        ret, val = pipe.pull()
        if ret:
            sum += val
            print('adding ' + str(val))
            print('current sum = ' + str(sum))


Thread(target=generator).start()
Thread(target=cumulative_adder).start()
