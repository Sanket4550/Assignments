import psutil
import sys
import os
import time
import smtplib
from email.message import EmailMessage

def CreateLog(directory):
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

    return filename

def SendMail(receiver, filepath):
    try:
        sender = "your_email@gmail.com"
        password = "your_app_password"

        msg = EmailMessage()
        msg['Subject'] = "Process Log File"
        msg['From'] = sender
        msg['To'] = receiver

        msg.set_content("Attached is the process log file.")

        with open(filepath, "rb") as f:
            msg.add_attachment(f.read(), maintype='application',
                               subtype='octet-stream',
                               filename=os.path.basename(filepath))

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Email Error:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: ProcInfoLog.py Directory Email")
        return

    logfile = CreateLog(sys.argv[1])
    SendMail(sys.argv[2], logfile)

if __name__ == "__main__":
    main()
