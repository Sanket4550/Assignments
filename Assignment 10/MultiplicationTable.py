def Multiplication(No):

    for i in range(1,11):
       # print(No * i)
        print(No * i, end=" ")   # print on same line
        i += 1

    
def main():
    Num = int(input("Enter a number : "))

    Ret = Multiplication(Num)

    

if __name__ == "__main__":
    main()