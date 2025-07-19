# Automate-File-Organiser
📌 Project Title:
Basic File Organizer Using Python

📝 Description:
This Python script is a basic automation tool that helps organize files inside a specific folder (python task1) by grouping them based on their file type (e.g., images, music, videos, Python files).

The script works by:

Scanning all files in the folder.

Checking the file extensions (e.g., .jpg, .mp3, .py).

Moving each file into a corresponding folder named:

Images for image files

Video for video files

Python for .py files

If a destination folder (like Images) does not already exist, it is automatically created.

✅ Key Features:
📁 Auto-Folder Creation: Creates folders only when needed (e.g., Images/, Music/).
🚀 Auto File Sorting: Moves files into the correct folders based on their extension.
❌ Skips Unsupported Files: Any file with an unknown extension (e.g., .txt, .docx) is ignored.
🔁 Loop-Based Processing: Efficiently processes all files in the selected directory.

🗂️ Supported File Types:
Folder	Extensions
Images	.png, .jpg, .jpeg, .webp
Video	.mp4
Python	.py

🧪 How It Works:
Suppose your folder contains:

pic.jpg

script.py

song.mp3

notes.txt

After running the script:

pic.jpg → moved to Images/

script.py → moved to Python/

song.mp3 → moved to Music/

notes.txt → Skipped

