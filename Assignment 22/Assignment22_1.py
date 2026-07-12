from multiprocessing import Pool

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_of_squares, numbers)

    print("Sum of Squares:")
    for n, ans in zip(numbers, result):
        print(f"1^2 + 2^2 + ... + {n}^2 = {ans}")

if __name__ == "__main__":
    main()