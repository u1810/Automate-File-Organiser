import os
import shutil
from datetime import datetime

# Root folder to scan
folder_path = r"C:\Users\ummul khair\OneDrive\Desktop\python_task1"

# Supported file types and their categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".svg", ".ini"],
    "Music": [".mp3", ".wav"],
    "Video": [".mp4", ".webm", ".mkv", ".avi", ".mov"],
    "Python": [".py", ".txt"]  # including .txt for logs
}

log_file_path = os.path.join(folder_path, "organizer_log.txt")
files_moved = 0
today_date = datetime.now().strftime("%Y-%m-%d")

try:
    script_name = os.path.basename(__file__)
except NameError:
    script_name = "main.py"  # fallback if __file__ not available

# Recursively walk through all folders
for root, _, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Skip directories and the script itself
        if filename == script_name:
            continue

        ext = os.path.splitext(filename)[1].lower()
        print(f"🔍 Checking file: {filename}, Extension: {ext}")

        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder, today_date)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                    created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"🗂️ Created folder: {folder}\\{today_date} at {created_time}")
                    with open(log_file_path, "a", encoding="utf-8") as log:
                        log.write(f"[{created_time}] Created folder '{folder}\\{today_date}'\n")

                new_location = os.path.join(target_folder, filename)
                shutil.move(file_path, new_location)
                move_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"📁 Moved '{filename}' → '{folder}\\{today_date}' at {move_time}")
                with open(log_file_path, "a", encoding="utf-8") as log:
                    log.write(f"[{move_time}] Moved '{filename}' → '{folder}\\{today_date}'\n")

                files_moved += 1
                break
        else:
            print(f"⏭️ Skipped: '{filename}' (unsupported file type)")

if files_moved == 0:
    print("⚠️ No matching files found to move.")
else:
    print(f"\n✅ Total files moved: {files_moved}")
