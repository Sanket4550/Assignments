import os

def main():
    FileName = input("Enter file name : ")
    Ret = os.path.exists(FileName)

    if Ret == True:
        print("File exist in directory")
    else:
        print("File do not exist in directory")

if __name__ == "__main__":
    main()
