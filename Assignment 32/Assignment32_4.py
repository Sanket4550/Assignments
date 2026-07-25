import os
import shutil
import time

src = input("Enter source directory: ")
dest = input("Enter destination directory: ")

while True:
    if os.path.isdir(src) and os.path.isdir(dest):
        files = os.listdir(src)

        for file in files:
            if file.endswith(".txt"):
                try:
                    shutil.copy(os.path.join(src, file), dest)

                    log = open("CopyLog.txt", "a")
                    log.write(f"Copied: {file} at {time.ctime()}\n")
                    log.close()

                except:
                    print("Error copying:", file)
    else:
        print("Invalid directories")

    time.sleep(600)
