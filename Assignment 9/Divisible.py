def Divisible(No):

    if (No % 3 == 0):
        if (No % 5 == 0):
            print("Divisible by 3 and 5")
        else:
            print("Not divisible by 3 and 5")

def main():
    Num = int(input("Enter a number : "))

    Ret = Divisible(Num)

    

if __name__ == "__main__":
    main()