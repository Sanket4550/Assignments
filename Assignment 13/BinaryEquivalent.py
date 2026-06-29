def Bin_Equivalent(Num):
    Place = 1
    Binary = 0

    while Num > 0:
        Digit = Num % 2
        Binary = Binary + Digit * Place
        Place *= 10
        Num = Num // 2

    
    return Binary



def main():

    Number = int(input("Enter your Number : "))

    Ret = Bin_Equivalent(Number)
    print("Your Binary Equivalent is : ",Ret)

if __name__ == "__main__":
    main()