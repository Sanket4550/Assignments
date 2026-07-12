from multiprocessing import Pool
import time

def sum_of_fifth_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
    return (n, total)

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    start = time.time()

    with Pool() as p:
        result = p.map(sum_of_fifth_powers, numbers)

    end = time.time()

    print("Sum of Fifth Powers:")
    for n, total in result:
        print(f"1^5 + 2^5 + ... + {n}^5 = {total}")

    print("\nExecution Time:", end - start, "seconds")

if __name__ == "__main__":
    main()