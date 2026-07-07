def SumOf_Digit(Num):
    Num = abs(Num)

    Total = 0
    while Num > 0:
        Total += Num % 10
        Num //= 10
    return Total

def main():
    number = int(input("Enter a number: "))
    print("Sum of digits:", SumOf_Digit(number))

if __name__ == "__main__":
    main()