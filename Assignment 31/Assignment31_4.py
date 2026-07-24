import time

def CreateLog():
    timestamp = time.ctime()
    filename = "MarvellousLog%s.txt" % timestamp

    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")

    fobj = open(filename, "w")
    fobj.write("Log file created successfully\n")
    fobj.write("Creation time : %s\n" % time.ctime())
    fobj.close()

    print("Log created :", filename)

def main():
    while True:
        CreateLog()
        time.sleep(600)

if __name__ == "__main__":
    main()
