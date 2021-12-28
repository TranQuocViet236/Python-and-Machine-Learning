import threading
import time


def function1():
    print('function1 started...')
    time.sleep(2)
    print('function1 ended...')

def function2():
    print('function2 started...')
    time.sleep(2)
    print('function2 ended...')

def function3():
    print('function3 started...')
    time.sleep(2)
    print('function3 ended...')

if __name__ == '__main__':
    x1 = threading.Thread(target = function1, args = ())
    x1.start()
    x2 = threading.Thread(target = function2, args = ())
    x2.start()
    x3 = threading.Thread(target = function3, args = ())
    x3.start()
    print('Thread count = {}'.format(threading.active_count()))
    print('Thread enumerate = {}'.format(threading.enumerate()))