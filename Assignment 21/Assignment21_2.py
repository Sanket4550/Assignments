import threading

class Maximum(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr

    def run(self):
        print("Maximum Element =", max(self.arr))


class Minimum(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr

    def run(self):
        print("Minimum Element =", min(self.arr))


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

t1 = Maximum(arr)
t2 = Minimum(arr)

t1.start()
t2.start()

t1.join()
t2.join()