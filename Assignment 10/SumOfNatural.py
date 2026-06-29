def SumOfN(No):
    Sum = 0
    
    for i in range(No + 1):
        Sum = Sum + i
    return Sum
        

    
def main():
    Num = int(input("Enter a number : "))

    Ret = SumOfN(Num)

    print("Sum is : ",Ret)

    

if __name__ == "__main__":
    main()