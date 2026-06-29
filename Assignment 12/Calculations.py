def Calculation(No1,Opr,No2):

    if (Opr == "+"):
        print(No1 + No2)

    elif (Opr == "-"):
        print(No1 - No2)

    elif (Opr == "*"):
        print(No1 * No2)

    elif (Opr == "/"):
        print(No1 / No2)

    else:
        print("Invalid Operator")
    



def main():
    Num1 = int(input("Enter First number : "))  
    Operator = input("Enter your Operator  : ")

    Num2= int(input("Enter Second number : "))

    Ret = Calculation(Num1,Operator,Num2)

    

if __name__ == "__main__":
    main()