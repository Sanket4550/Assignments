from functools import reduce
MinElements = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    Data = [12, 23, 34, 43, 22, 51 ,54, 38]



    print(Data)

    Rdata = reduce(MinElements,Data)

   

    print("Minimun elements in the list is : ",Rdata)

if __name__ == "__main__":
    main()