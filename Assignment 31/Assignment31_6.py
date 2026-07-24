import time
import schedule

def Message1():
    print("Start your weekly goal")

def Message2():
    print("Review your weekly progress")

def Message3():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(Message1)
    schedule.every().wednesday.at("17:00").do(Message2)
    schedule.every().monday.at("18:00").do(Message3)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
