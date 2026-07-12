from multiprocessing import Pool
import math
import os

def factorial_info(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    numbers = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_info, numbers)

    print("Process ID\tInput\tFactorial")
    for pid, num, fact in result:
        print(pid, "\t", num, "\t", fact)

if __name__ == "__main__":
    main()