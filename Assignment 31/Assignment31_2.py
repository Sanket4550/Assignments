import time
import schedule

def DisplayMessage(message):
    print(message)

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    msg = input("Enter message : ")

    schedule.every(5).seconds.do(DisplayMessage, msg)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
