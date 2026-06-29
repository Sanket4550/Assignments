def Count_digit(Num):
    count = 0

    if Num == 0:
        return 1
    
    while Num != 0:
        Num = Num // 10
        count += 1

    return count

def main():

    Number = int(input("Enter your Number : "))

    Ret = Count_digit(Number)
    print("Your count is : ",Ret)

if __name__ == "__main__":
    main()