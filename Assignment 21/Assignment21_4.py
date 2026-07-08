import threading

class SumThread(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr
        self.total = 0

    def run(self):
        self.total = sum(self.arr)


class ProductThread(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr
        self.product = 1

    def run(self):
        for i in self.arr:
            self.product *= i


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

t1 = SumThread(arr)
t2 = ProductThread(arr)

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", t1.total)
print("Product =", t2.product)