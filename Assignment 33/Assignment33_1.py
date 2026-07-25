import os
import sys
import time
import hashlib
import schedule
import smtplib
from email.message import EmailMessage
from datetime import datetime

def CalculateChecksum(path, blocksize=1024):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = file.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = file.read(blocksize)
    file.close()
    return hasher.hexdigest()

def FindDuplicates(directory):
    duplicates = {}
    file_count = 0
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(folder, file)
            file_count += 1
            try:
                checksum = CalculateChecksum(file_path)
                if checksum in duplicates:
                    duplicates[checksum].append(file_path)
                else:
                    duplicates[checksum] = [file_path]
            except:
                continue
    return duplicates, file_count

def DeleteDuplicates(duplicates, log_file):
    deleted_count = 0
    for checksum in duplicates:
        files = duplicates[checksum]
        if len(files) > 1:
            for file in files[1:]:
                try:
                    os.remove(file)
                    log_file.write(f"Deleted: {file}\n")
                    deleted_count += 1
                except:
                    log_file.write(f"Error deleting: {file}\n")
    return deleted_count

def CreateLog():
    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    log_name = f"Marvellous/DuplicateLog_{timestamp}.log"
    return open(log_name, "w"), log_name

def SendEmail(receiver, log_file_path, stats):
    try:
        sender_email = "your_email@gmail.com"
        password = "your_app_password"
        msg = EmailMessage()
        msg['Subject'] = "Duplicate File Removal Report"
        msg['From'] = sender_email
        msg['To'] = receiver
        body = f"""Duplicate File Removal Completed

Starting Time : {stats['start']}
Completion Time : {stats['end']}
Directory : {stats['directory']}
Total Files Scanned : {stats['total']}
Duplicates Found : {stats['duplicates']}
Duplicates Deleted : {stats['deleted']}"""
        msg.set_content(body)
        with open(log_file_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=log_file_path)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
    except:
        pass

def DirectoryWatcher(directory, email):
    start_time = time.ctime()
    log_file, log_path = CreateLog()
    log_file.write(f"Start Time: {start_time}\n")
    log_file.write(f"Directory: {directory}\n")
    duplicates, total_files = FindDuplicates(directory)
    duplicate_count = sum(len(v)-1 for v in duplicates.values() if len(v) > 1)
    deleted_count = DeleteDuplicates(duplicates, log_file)
    end_time = time.ctime()
    log_file.write(f"\nTotal Files: {total_files}\n")
    log_file.write(f"Duplicate Files Found: {duplicate_count}\n")
    log_file.write(f"Deleted Files: {deleted_count}\n")
    log_file.write(f"End Time: {end_time}\n")
    log_file.close()
    stats = {
        "start": start_time,
        "end": end_time,
        "directory": directory,
        "total": total_files,
        "duplicates": duplicate_count,
        "deleted": deleted_count
    }
    SendEmail(email, log_path, stats)

def StartScheduler(directory, interval, email):
    schedule.every(interval).minutes.do(DirectoryWatcher, directory, email)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    if len(sys.argv) != 4:
        print("Usage:")
        print("python DuplicateFileRemoval.py <Directory> <IntervalMinutes> <Email>")
        exit()
    directory = sys.argv[1]
    interval = int(sys.argv[2])
    email = sys.argv[3]
    if not os.path.exists(directory):
        print("Invalid directory")
        exit()
    if interval <= 0:
        print("Interval must be greater than 0")
        exit()
    StartScheduler(directory, interval, email)

if __name__ == "__main__":
    main()
