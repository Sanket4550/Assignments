def Frequency(lst, no):
    count = 0

    for i in lst:
        if i == no:
            count = count + 1

    return count


def main():
    n = int(input("Enter number of elements: "))

    data = []

    for i in range(n):
        value = int(input())
        data.append(value)

    no = int(input("Enter number to search: "))

    ans = Frequency(data, no)

    print("Frequency is:", ans)


if __name__ == "__main__":
    main()