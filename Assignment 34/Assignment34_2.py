import psutil
import sys

def FindProcess(proc_name):
    found = False

    for proc in psutil.process_iter(['name']):
        try:
            if proc_name.lower() in proc.info['name'].lower():
                found = True
                print(f"{proc_name} is running (PID: {proc.pid})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    if not found:
        print(f"{proc_name} is NOT running")

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfo.py ProcessName")
        return

    FindProcess(sys.argv[1])

if __name__ == "__main__":
    main()
