import time
import schedule

def MorningMessage():
    print("Namaskar..!")

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every().day.at("09:00").do(MorningMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
