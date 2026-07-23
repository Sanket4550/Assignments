# Assignment 30 - Script 7 (Backup Script)

import time
import schedule
from datetime import datetime
import sys
import shutil
import os

def BackUpFile(src, dest):

    if not os.path.exists(src):
        print("Source file does not exist")
        return

    if not os.path.exists(dest):
        os.mkdir(dest)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    filename = os.path.basename(src)
    name, ext = os.path.splitext(filename)

    newname = dest + "/" + name + "_" + timestamp + ext

    shutil.copy(src, newname)

    with open("backup_log.txt", "a") as fobj:
        fobj.write("Backup completed successfully at " + 
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print("Backup Done")

def main():
    border = "-"*30

    print(border)
    print("Automation Script")
    print(border)

    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file> <destination_folder>")
        return

    src = sys.argv[1]
    dest = sys.argv[2]

    schedule.every(1).hours.do(BackUpFile, src, dest)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
