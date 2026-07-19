def main():
    try:
        FileName = input("Enter file name : ")
        fobj = open(FileName,'r')
        count = 0
        for line in fobj:
            count += 1
        print(count)
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
