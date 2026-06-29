def Calculation(No):

    for i in range (1, No + 1):
        print(i, end = " ")

    

def main():
    Num1 = int(input("Enter number : "))  

    Ret = Calculation(Num1)

    

if __name__ == "__main__":
    main()