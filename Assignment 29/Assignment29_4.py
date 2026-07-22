import sys

def main():

    if len(sys.argv) != 3:
        print("Usage : python program.py File1 File2")
        return

    fname1 = sys.argv[1]
    fname2 = sys.argv[2]

    try:
        f1 = open(fname1, "r")
        f2 = open(fname2, "r")

        data1 = f1.read()
        data2 = f2.read()

        f1.close()
        f2.close()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

    except FileNotFoundError:
        print("File does not exist")

if __name__ == "__main__":
    main()
