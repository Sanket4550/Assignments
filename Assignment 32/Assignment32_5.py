import os
import time

def DeleteEmpty(path):
    log = open("DeleteLog.txt", "a")

    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)

            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)
                    log.write(f"Deleted: {filepath} at {time.ctime()}\n")
                    print("Deleted:", filepath)

            except PermissionError:
                print("Permission denied:", filepath)

    log.close()

directory = input("Enter directory path: ")

while True:
    DeleteEmpty(directory)
    time.sleep(3600)
