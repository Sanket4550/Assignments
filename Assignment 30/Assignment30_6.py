import time
import schedule

def LunchTime():
    print("Lunch time !")

def WrapUp():
    print("Wrap up work")

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
