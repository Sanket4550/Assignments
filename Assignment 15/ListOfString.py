
ListOfString = lambda Str : len(Str) > 5

def main():
    Data = ["apple", "banana", "grapes", "watermelon", "kiwi", "pineapple", "fig"]
    print("List of strings is : ")
    print(Data)

    Fdata = list(filter(ListOfString,Data))

    print(" Strings whose length is greater than 5 is : ",Fdata)

if __name__ == "__main__":
    main()