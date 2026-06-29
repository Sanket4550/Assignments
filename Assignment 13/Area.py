Rectangle_Area = lambda Num1,Num2 : Num1 * Num2



def main():


    Length = float(input("Enter rectangle length : "))

    Width = float(input("Enter rectangle width : "))


    Ret = Rectangle_Area(Length,Width)
    print("Area of a rectangle is : ",Ret)
    

if __name__ == "__main__":
    main()