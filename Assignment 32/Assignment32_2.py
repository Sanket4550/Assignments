import os
import time

filename = input("Enter file path: ")

while True:
    f = open("FileSizeLog.txt", "a")

    if os.path.exists(filename):
        size = os.path.getsize(filename)
        f.write(f"{filename} | Size: {size} bytes | Time: {time.ctime()}\n")
        print("Logged size")
    else:
        f.write(f"{filename} | File not found | Time: {time.ctime()}\n")
        print("File not found")

    f.close()
    time.sleep(30)
