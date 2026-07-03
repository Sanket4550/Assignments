from functools import reduce
ProductOfElements = lambda No1,No2 : No1 * No2

def main():
    Data = [12, 23, 34, 43, 22, 51 ,54, 38]

    print(Data)

    Rdata = reduce(ProductOfElements,Data)

    print("Product of all numbers in the list is : ",Rdata)

if __name__ == "__main__":
    main()