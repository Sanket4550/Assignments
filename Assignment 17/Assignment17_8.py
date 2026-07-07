def Pattern2(n):
    Count = 1
    for i in range (1,n + 1):
        for j in range (1,Count + 1):
            print(j,end =" ")
        Count += 1
        print()

def main():
    Num = int(input("Enter value : "))

    Pattern2(Num)

if __name__ == "__main__":
    main()