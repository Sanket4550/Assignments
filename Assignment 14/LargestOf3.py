Largest = lambda No1,No2,No3 : max(No1,No2,No3)


def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))
    Num3 = int(input("Enter second number : "))


    Ret = Largest(Num1,Num2,Num3)

    print("Largest number is : ",Ret)

    

if __name__ == "__main__":
    main()