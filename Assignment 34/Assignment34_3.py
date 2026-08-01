import psutil
import sys
import os
import time

def CreateLog(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)

        filename = os.path.join(directory, "ProcessLog_%s.log" %
                                time.strftime("%Y%m%d_%H%M%S"))

        with open(filename, "w") as f:
            f.write("Name\tPID\tUsername\n")
            f.write("-" * 50 + "\n")

            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    f.write(f"{proc.info['name']}\t{proc.info['pid']}\t{proc.info['username']}\n")
                except:
                    pass

        print("Log file created at:", filename)

    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfoLog.py DirectoryName")
        return

    CreateLog(sys.argv[1])

if __name__ == "__main__":
    main()
