from multiprocessing import Pool
import os

def Factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Factorial :", fact)
    print()

if __name__ == "__main__":
    Data = [10, 15, 20, 25]

    p = Pool()
    p.map(Factorial, Data)

    p.close()
    p.join()