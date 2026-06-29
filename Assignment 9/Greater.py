def ChkGreater(Value1,Value2):

    if (Value1 > Value2):
        return Value1
    else:
        return Value2
    
    
    

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = ChkGreater(No1,No2)

    print("Greater number is : ",Ret)

if __name__ == "__main__":
    main()