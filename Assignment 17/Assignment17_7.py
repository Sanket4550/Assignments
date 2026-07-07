def Pattern2(n):
    for i in range (1,n+1):
        for j in range (1,n+1):
            print(j,end =" ")
        print()

def main():
    Num = int(input("Enter value : "))

    Pattern2(Num)

if __name__ == "__main__":
    main()