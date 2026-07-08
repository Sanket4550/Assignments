def ListSum(lst):
    total = 0

    for i in lst:
        total = total + i

    return total


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    ans = ListSum(data)

    print("Addition is:", ans)


if __name__ == "__main__":
    main()