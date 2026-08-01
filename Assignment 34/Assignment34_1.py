import psutil

def DisplayProcesses():
    try:
        print("{:<25} {:<10} {:<20}".format("Name", "PID", "Username"))
        print("-" * 60)

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                print("{:<25} {:<10} {:<20}".format(
                    proc.info['name'],
                    proc.info['pid'],
                    str(proc.info['username'])
                ))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

    except Exception as e:
        print("Error:", e)

def main():
    DisplayProcesses()

if __name__ == "__main__":
    main()
