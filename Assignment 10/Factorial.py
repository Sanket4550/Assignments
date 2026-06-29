def Fact(No):
    Ans = 1
    
    for i in range(1,No + 1):
        Ans = Ans * i
        
    return Ans
        

    
def main():
    Num = int(input("Enter a number : "))

    Ret = Fact(Num)

    print("Factorial is : ",Ret)

    

if __name__ == "__main__":
    main()