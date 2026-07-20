def main():
    try:
        From = input("Enter source file name : ")
        To = input("Enter destination file name : ")
        source = open(From,'r')
        data = source.read()
        destination = open(To,'w')
        destination.write(data)
        print("File Copied Successfully")
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
