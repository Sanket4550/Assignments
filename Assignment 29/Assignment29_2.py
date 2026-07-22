def main():
    try:
        FileName = input("Enter file name : ")

        dobj = open(FileName, "r")
        print("File opened")

        data = dobj.read()
        print(data)

        dobj.close()

    except FileNotFoundError:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
