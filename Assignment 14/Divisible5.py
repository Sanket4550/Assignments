CheckDivisible = lambda No1 : No1 % 5 == 0


def main():
    Num1 = int(input("Enter number : "))
    
    Ret = CheckDivisible(Num1)

    print(Ret)
   

    

if __name__ == "__main__":
    main()