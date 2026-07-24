import os
import time
import schedule

def CountFiles(DirName):
    if os.path.exists(DirName):
        count = 0
        for root, dirs, files in os.walk(DirName):
            count += len(files)

        timestamp = time.ctime()

        with open("DirectoryCountLog.txt", "a") as fobj:
            fobj.write("Directory : " + DirName + "\n")
            fobj.write("Number of files : " + str(count) + "\n")
            fobj.write("Time : " + timestamp + "\n")
            fobj.write("--------------------------------------\n")

        print("Updated log at:", timestamp)
    else:
        print("Directory not found")

def main():
    DirName = input("Enter directory name : ")
    schedule.every(5).minutes.do(CountFiles, DirName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
