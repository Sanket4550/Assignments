def ChkNum(no):
    if  no%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    value = int(input("Enter a  number"))
    ChkNum(value)

if __name__ == "__main__":
    main()