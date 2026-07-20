def main():
    try:
        FileName = input("Enter file name : ")
        fobj = open(FileName,'r')
        for line in fobj:
            print(line.strip())
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
