# Automate-File-Organiser
# 🗂️ Automated File Organizer

This Python script automatically organizes files by type (Images, Videos, Music, Python files, etc.) and sorts them into dated folders. It's especially useful for cleaning up cluttered directories like the Desktop or Downloads.

---

## 📌 Features

- ✅ Recursively scans all files in the target folder and its subfolders
- 📂 Automatically creates folders for each file type (e.g., `Images`, `Videos`, etc.)
- 📅 Organizes files into subfolders by current date (e.g., `Images/2025-07-19`)
- 📝 Maintains a log of all actions in `organizer_log.txt`
- 🔄 Supports common formats like `.jpg`, `.mp4`, `.py`, `.txt`, etc.

---

## 🔧 How It Works

1. Place the script in the folder you want to organize or set the path manually.
2. Run the script.
3. All supported files will be moved into dated subfolders inside their type-based categories.
4. Unsupported files are skipped (with a message).
5. A log is maintained in `organizer_log.txt`.

---

## 🗃️ Supported File Types

| Category | Extensions |
|----------|------------|
| Images   | `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.ini` |
| Videos   | `.mp4`, `.webm`, `.mkv`, `.avi`, `.mov` |
| Music    | `.mp3`, `.wav` |
| Python   | `.py`, `.txt` |

---

## ▶️ How to Run

### Step 1: Install Python
Make sure Python 3 is installed on your system.  
You can download it from: https://www.python.org/downloads/

### Step 2: Run the Script

Open a terminal or PowerShell and run:

```bash
python main.py

🔍 Files Processed:
| File Name                                                                         | Type   | Destination Folder  |
| --------------------------------------------------------------------------------- | ------ | ------------------- |
| `organizer_log.txt`                                                               | Python | `Python\2025-07-19` |
| `desktop.ini`                                                                     | Image  | `Images\2025-07-19` |
| `kha.jpg`                                                                         | Image  | `Images\2025-07-19` |
| `umm.jpg`                                                                         | Image  | `Images\2025-07-19` |
| `WhatsApp Audio 2025-07-11 at 16.37.53_b5873059 (online-audio-converter.com).mp3` | Music  | `Music\2025-07-19`  |
| `organizer_log.txt` (second move due to duplication or source reset)              | Python | `Python\2025-07-19` |

📁 Output Folder Structure:
python_task1/
│
├── Images/
│   └── 2025-07-19/
│       ├── kha.jpg
│       ├── umm.jpg
│       └── desktop.ini
│
├── Music/
│   └── 2025-07-19/
│       └── WhatsApp Audio ....mp3
│
├── Python/
│   └── 2025-07-19/
│       └── organizer_log.txt
│
├── Python/
│   └── main.py

📝 Final Result:
✅ Total Files Moved: 6
📂 Organized into: Images, Music, Python (each with 2025-07-19 folder)
🧠 Log File: Updated with all actions inside organizer_log.txt

