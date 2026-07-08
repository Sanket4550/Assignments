import threading

def EvenFactor(num):
    print("Even Factors:")
    total = 0

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            print(i, end=" ")
            total += i

    print("\nSum of Even Factors:", total)


def OddFactor(num):
    print("Odd Factors:")
    total = 0

    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            print(i, end=" ")
            total += i

    print("\nSum of Odd Factors:", total)


def main():
    no = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(no,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(no,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()