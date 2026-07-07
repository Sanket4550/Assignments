def IsPrime(No):
    

    

    if No < 2:
        return False
    
    for i in range(2,int(No**0.5) + 1): #to check upto square root
        if No % i == 0:
            return False
    return True
            

def main():
    Num = int(input("Enter number : "))

    if IsPrime(Num):
        print("Prime")
    else:
        print("Not Prime")
       

if __name__ == "__main__":
    main()