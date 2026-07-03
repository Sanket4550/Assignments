ListOfOdd = lambda No : No % 2 != 0

def main():
    Data = [12, 23, 34, 43, 22, 51 ,54, 37]

    print(Data)

    Fdata = list(filter(ListOfOdd,Data))

    print("List of odd numbers is : ",Fdata)

if __name__ == "__main__":
    main()