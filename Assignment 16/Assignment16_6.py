def CheckNum(no):
    if no>0:
        print("positive number")
    elif no<0:
        print("negative number")
    else:
        print("zero")

def main():
    num = int(input("enter a number"))
    CheckNum(num)


if __name__ == "__main__":
    main()