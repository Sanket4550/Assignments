from multiprocessing import Pool
import os

def CountOdd(n):
    count = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Odd Number Count :", count)
    print()

if __name__ == "__main__":
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()
    p.map(CountOdd, Data)

    p.close()
    p.join()