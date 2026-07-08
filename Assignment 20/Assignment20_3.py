import threading

def EvenList(arr):
    even = []
    total = 0

    for i in arr:
        if i % 2 == 0:
            even.append(i)
            total += i

    print("Even Elements:", even)
    print("Sum of Even Elements:", total)


def OddList(arr):
    odd = []
    total = 0

    for i in arr:
        if i % 2 != 0:
            odd.append(i)
            total += i

    print("Odd Elements:", odd)
    print("Sum of Odd Elements:", total)


def main():
    n = int(input("Enter number of elements: "))

    arr = []
    print("Enter elements:")
    for i in range(n):
        arr.append(int(input()))

    t1 = threading.Thread(target=EvenList, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(arr,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()