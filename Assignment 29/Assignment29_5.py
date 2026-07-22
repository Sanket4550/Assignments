import sys

def main():

    if len(sys.argv) != 3:
        print("Usage : python program.py FileName String")
        return

    fname = sys.argv[1]
    word = sys.argv[2]

    try:
        file = open(fname, "r")
        data = file.read()
        file.close()

        count = data.count(word)

        print("Frequency of", word, "is :", count)

    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()
