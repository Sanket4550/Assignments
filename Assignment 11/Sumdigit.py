def Sumof_digit(Num):
    Sum = 0
    
    while Num > 0:
        digit = Num % 10
        Sum = Sum + digit
        Num = Num // 10


    return Sum

def main():

    Number = int(input("Enter your Number : "))

    Ret = Sumof_digit(Number)
    print("Your sum is : ",Ret)

if __name__ == "__main__":
    main()