def Fact(Num):

    for i in range(1, Num + 1, 1):
        if Num % i == 0:
            print(i, end= " ")


def main():

    Number = int(input("Enter your Number : "))

    Ret = Fact(Number)
    

if __name__ == "__main__":
    main()