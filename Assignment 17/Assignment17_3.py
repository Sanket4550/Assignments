def Fact(no):
    Ans = 1

    for i in range(1,no+1):
        Ans *= i
    return Ans

def main():
    Num = int(input("Enter number : "))

    Ret = Fact(Num)
    print("Factorial of",Num," is : ",Ret)

if __name__ == "__main__":
    main()