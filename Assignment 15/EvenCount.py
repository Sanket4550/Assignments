from functools import reduce
ListOfEven = lambda No : No % 2 == 0

def main():
    Data = [12, 23, 34, 43, 22, 51 ,54, 37, 42]

    print(Data)

    Fdata = list(filter(ListOfEven,Data))

    Rdata = len(Fdata)

    print("List of even numbers is : ",Fdata)
    print("Count of even numbers are : ",Rdata)

if __name__ == "__main__":
    main()