import time
import schedule

def CodingMessage():
    print("Coding kar..!")

def main():
    border = "-" * 30

    print(border)
    print("Automation Script")
    print(border)

    schedule.every(30).minutes.do(CodingMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
