def Minimum(lst):
    min = lst[0]

    for i in lst:
        if i < min:
            min = i

    return min


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    ans = Minimum(data)

    print("Minimum number is:", ans)


if __name__ == "__main__":
    main()