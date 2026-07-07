import Arithmetic as AR

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter first number : "))

    Ret = AR.Add(Num1,Num2)
    print("Addition is : ",Ret)

    Ret = AR.Sub(Num1,Num2)
    print("Subtraction is : ",Ret)

    Ret = AR.Mult(Num1,Num2)
    print("Multiplication is : ",Ret)

    Ret = AR.Div(Num1,Num2)
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()