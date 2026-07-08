import threading

class Prime(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def run(self):
        print("Prime Numbers:")
        for i in self.arr:
            if self.isPrime(i):
                print(i, end=" ")
        print()


class NonPrime(threading.Thread):
    def __init__(self, arr):
        threading.Thread.__init__(self)
        self.arr = arr

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def run(self):
        print("Non-Prime Numbers:")
        for i in self.arr:
            if not self.isPrime(i):
                print(i, end=" ")
        print()


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

t1 = Prime(arr)
t2 = NonPrime(arr)

t1.start()
t2.start()

t1.join()
t2.join()