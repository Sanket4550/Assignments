import time
import os
import schedule

def DirectoryScanner(path):
    files = 0
    dirs = 0

    try:
        for entry in os.listdir(path):
            fullpath = os.path.join(path, entry)

            if os.path.isfile(fullpath):
                files += 1
            elif os.path.isdir(fullpath):
                dirs += 1

        print("Directory Scanned :", path)
        print("Total Files :", files)
        print("Total subdirectories :", dirs)
        print("Scan Time :", time.ctime())
        print("-" * 30)

    except Exception as e:
        print("Error :", e)

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    path = input("Enter directory path : ")

    schedule.every(60).seconds.do(DirectoryScanner, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
