def Pattern(n):
    for i in range (n):
        for j in range (n):
            print("*",end =" ")
        print()

def main():
    star = int(input("Enter value : "))

    Pattern(star)

if __name__ == "__main__":
    main()