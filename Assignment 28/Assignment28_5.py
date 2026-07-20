def main():
    try:
        FileName = input("Enter file name : ")
        Word = input("Enter word to search : ")
        found = False
        file = open(FileName,'r')
        for line in file:
            if Word in line:
                found = True
                break
        if found:
            print("Word found in file")
        else:
            print("Word not found in file")
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
