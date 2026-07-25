import time
import os

filename = input("Enter file name: ")

while True:
    try:
        if not os.path.exists(filename):
            print("File does not exist")
        else:
            f = open(filename, "r")
            data = f.read()

            if data == "":
                print("File is empty")
            else:
                print("Content:\n", data)

            f.close()

    except PermissionError:
        print("Permission denied")
    except:
        print("File cannot be opened")

    time.sleep(60)
