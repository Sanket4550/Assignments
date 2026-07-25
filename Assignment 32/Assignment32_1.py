import time

while True:
    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"File_{timestamp}.txt"

    f = open(filename, "w")
    f.write(f"Filename : {filename}\n")
    f.write(f"Creation Date : {time.strftime('%d-%m-%Y')}\n")
    f.write(f"Creation Time : {time.strftime('%H:%M:%S')}\n")
    f.close()

    print("Created:", filename)
    time.sleep(60)
