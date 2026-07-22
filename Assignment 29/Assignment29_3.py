import sys

def main():

    if len(sys.argv) != 2:
        print("Usage : python program.py FileName")
        return

    source = sys.argv[1]

    try:
        file1 = open(source, "r")
        data = file1.read()
        file1.close()

        file2 = open("Demo.txt", "w")
        file2.write(data)
        file2.close()

        print("Content copied successfully")

    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()
