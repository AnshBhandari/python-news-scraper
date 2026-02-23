import schedule
import time
import subprocess
import sys
import os

# Path to your main script
SCRIPT_PATH = r"<Path_to_your_main_script>\main.py"

def run_script():
    print("Running daily script...")
    subprocess.run([sys.executable, SCRIPT_PATH])

# Set the time here (24-hour format)
schedule.every().day.at("20:00").do(run_script)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(30)
