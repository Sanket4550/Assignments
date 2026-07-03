CheckOdd = lambda No1 : No1 % 2 != 0


def main():
    Num1 = int(input("Enter number : "))
    
    Ret = CheckOdd(Num1)

    print(Ret)
   

    

if __name__ == "__main__":
    main()