def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def ListPrime(lst):
    total = 0

    for i in lst:
        if ChkPrime(i):
            total = total + i

    return total


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    ans = ListPrime(data)

    print("Addition of prime numbers is:", ans)


if __name__ == "__main__":
    main()