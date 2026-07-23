import time
import schedule
import datetime

def PrintToFile():
    now = datetime.datetime.now()
    fobj = open("Marvellous.txt", "a")
    fobj.write("Task executed at : " + now.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every(5).minutes.do(PrintToFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
