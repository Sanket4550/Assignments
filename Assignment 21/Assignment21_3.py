import threading

counter = 0
lock = threading.Lock()

class CounterThread(threading.Thread):
    def run(self):
        global counter

        for i in range(100000):
            lock.acquire()
            counter += 1
            lock.release()


t1 = CounterThread()
t2 = CounterThread()
t3 = CounterThread()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final Counter Value =", counter)