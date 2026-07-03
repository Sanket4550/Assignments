Sqr = lambda No : No * No

def main():
    Data = [12, 23, 34, 43, 22, 56 ,54]

    print(Data)

    Mdata = list(map(Sqr,Data))

    print("List after Square of each number is : ",Mdata)

if __name__ == "__main__":
    main()