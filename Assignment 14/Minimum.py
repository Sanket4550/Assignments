Min = lambda No1,No2 : No1 < No2


def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))

    Ret = Min(Num1,Num2)

    if (Ret == True):
        print("Minimum No between ",Num1," And ",Num2," is : ",Num1)
    else:
        print("Minimum No between ",Num1," And ",Num2," is : ",Num2)

    

if __name__ == "__main__":
    main()