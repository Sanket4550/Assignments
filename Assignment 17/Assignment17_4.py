def Factors(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum += i
    return Sum



def main():
    Num = int(input("Enter number : "))

    Ret = Factors(Num)
    print("Addition of factors of",Num," is : ",Ret)

if __name__ == "__main__":
    main()