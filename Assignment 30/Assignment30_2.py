import time
import schedule
import datetime

def PrintTime():
    now = datetime.datetime.now()
    print("Current Date and Time :", now.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every(1).minutes.do(PrintTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
