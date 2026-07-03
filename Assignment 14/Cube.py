Cube = lambda No : (No * No) * No


def main():
    Num = int(input("Enter your number : "))

    Ret = Cube(Num)

    print("Your Cube is : ",Ret)

if __name__ == "__main__":
    main()