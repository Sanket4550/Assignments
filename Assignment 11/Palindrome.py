def Reverse(Num):
    Reverse_Num = 0

    while Num > 0:
        Digit = Num % 10
        Reverse_Num = Reverse_Num * 10 + Digit
        Num = Num // 10

    return Reverse_Num


def main():

    Number = int(input("Enter your Number : "))

    Ret = Reverse(Number)

    if (Ret == Number):
        print("Palindrome")
    else:
        print("Non palindrome")
    

if __name__ == "__main__":
    main()