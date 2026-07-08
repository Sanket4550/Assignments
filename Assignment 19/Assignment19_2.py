def Maximum(lst):
    max = lst[0]

    for i in lst:
        if i > max:
            max = i

    return max


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    ans = Maximum(data)

    print("Maximum number is:", ans)


if __name__ == "__main__":
    main()