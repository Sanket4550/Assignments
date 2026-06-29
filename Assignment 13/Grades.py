def Grade(Marks):
    if (100 > Marks >= 75):
        return "Distinction"
    elif (Marks >= 60):
        return "First Class"

    elif (Marks >= 50):
        return "Second Class"

    else:
        return "Fail"

def main():


    Num = int(input("Enter Marks : "))

    Ret = Grade(Num)
    print("Grade is : ",Ret)
    

if __name__ == "__main__":
    main()