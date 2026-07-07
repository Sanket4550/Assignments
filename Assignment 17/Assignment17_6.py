def Pattern(n):
    Count = n
    for i in range (0,n):
        for j in range (Count,0,-1):
            print("* ",end =" ")
        Count -= 1
        print()

def main():
    star = int(input("Enter value : "))

    Pattern(star)

if __name__ == "__main__":
    main()