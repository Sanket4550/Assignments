import time
import schedule

def PrintMessage():
    print("Jay Ganesh...")

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every(2).seconds.do(PrintMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
