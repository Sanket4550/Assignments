def Is_Perfect(Num):

    Sum = 0

    for i in range(1,Num):
        if Num % i == 0:
            Sum += i

    return Sum


def main():

    Number = int(input("Enter your number : "))

    Ret = Is_Perfect(Number)

    if Ret == Number :
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    
  

if __name__ == "__main__":
    main()