def Counter(No):

    No = abs(No)
    if No == 0:
        return 1

    Count = 0
    while No > 0:
        No //= 10
        Count += 1
    return Count



def main():
    Num = int(input("Enter value : "))

    Ret = Counter(Num)

    print("Number of digits in number is : ",Ret)


if __name__ == "__main__":
    main()