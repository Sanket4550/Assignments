from multiprocessing import Pool
import os

def SumOdd(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Odd Numbers :", total)
    print()

if __name__ == "__main__":
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()
    p.map(SumOdd, Data)

    p.close()
    p.join()