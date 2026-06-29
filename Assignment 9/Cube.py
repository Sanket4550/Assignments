def Cube(No):
    return No*No*No

def main():
    Num = int(input("Enter a number : "))

    Ret = Cube(Num)

    print("Square of given number is : ",Ret)

if __name__ == "__main__":
    main()