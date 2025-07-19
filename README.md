# Automate-File-Organiser
Absolutely! Here's how your **💼 Automated File Organizer Project** would look when documented in the same professional format as the chat app description you provided.

---

## 📁 Automated File Organizer (Python)

This is a **file organization automation script** written in Python. It scans a selected folder, detects files based on their extensions (e.g., `.py`, `.jpg`, `.mp3`), and automatically moves them into categorized folders such as `Images`, `Music`, `Video`, and `Python`. It also creates date-based subfolders and logs every move.

---

### ✅ Features

* 🗂️ **Auto-folder creation** based on file type
* 📅 **Date-based subfolder** organization (e.g., `Images/2025-07-16/`)
* 🔁 **Processes all files** in the selected folder
* 🚫 **Skips unsupported file types** like `.txt`, `.ini`
* 🧠 **Avoids moving itself** (`main.py`)
* 📝 **Activity logged** in `organizer_log.txt`
* 💻 Easy to run on any system with Python installed

---

### 🛠️ Tech Stack

* **Python 3.x** (core logic)
* **OS & Shutil modules** (file operations)
* **Datetime** (for folder timestamps)

---

### 📁 Project Structure

```
python-task1/
├── main.py              # Main Python script (organizer)
├── create_test_files.py # (Optional) creates dummy files for testing
├── organizer_log.txt    # Log file (auto-created)
├── Images/
│   └── 2025-07-16/      # Example subfolder for images
├── Python/
│   └── 2025-07-16/      # Example subfolder for .py files
└── ...
```

---

### 🚀 How to Run

#### 1️⃣ Install Python

Ensure Python 3.x is installed on your system. You can check using:

```bash
python --version
```

#### 2️⃣ (Optional) Create test files

Use this helper script to generate dummy files:

```bash
python create_test_files.py
```

#### 3️⃣ Run the File Organizer

```bash
python main.py
```

#### 4️⃣ View Organized Files

Check the folders like `Images/`, `Video/`, `Python/`, and their date-based subfolders.

---

### 🌐 Sample Output

```bash
🗂️ Created folder: Python\2025-07-16 at 2025-07-16 18:23:10
📁 Moved 'test.py' → 'Python\2025-07-16' at 2025-07-16 18:23:10
📁 Moved 'song1.mp3' → 'Music\2025-07-16' at 2025-07-16 18:23:10
✅ Total files moved: 4
```

---

Would you like this entire project summary exported as a **PDF or `README.md` file** for submission or GitHub?


