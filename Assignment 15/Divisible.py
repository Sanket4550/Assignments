Divisible = lambda No : No % 3 == 0 | No % 5 ==0

def main():
    Data = [15, 23, 30, 43, 22, 75 ,54, 37]

    print(Data)

    Fdata = list(filter(Divisible,Data))

    print("numbers divisible by 3 and 5 are : ",Fdata)

if __name__ == "__main__":
    main()