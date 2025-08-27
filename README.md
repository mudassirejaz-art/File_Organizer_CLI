# 📂 File Organizer CLI

An **advanced Python CLI tool** to organize files in a directory by **type, creation date, or size**. Includes logging, dry-run mode, and automated tests with pytest.

---

## ✨ Features

* Organize files by **type** (Images, Documents, Audio, Video, Archives, Others)
* Organize files by **creation date** (YYYY-MM-DD folders)
* Organize files by **size** (Small, Medium, Large)
* **Dry-run mode** → preview without moving files
* **Logging support** → generates `organizer.log`
* **Configurable CLI arguments** with `argparse`
* **Unit tests included** with `pytest`

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/mudassirejaz-art/File_Organizer_CLI.git
cd File_Organizer_CLI

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Organize by Type

```bash
python src/organizer.py --path ./test_files --mode type
```

### Organize by Date

```bash
python src/organizer.py --path ./test_files --mode date
```

### Organize by Size

```bash
python src/organizer.py --path ./test_files --mode size
```

### Dry Run (safe preview)

```bash
python src/organizer.py --path ./test_files --mode type --dry-run
```

---

## 🧪 Running Tests

```bash
# Install pytest
pip install pytest

# Run tests
PYTHONPATH=src pytest -v
```

---

## 📁 Project Structure

```
File_Organizer_CLI/
│── src/
│   ├── organizer.py
│   └── __init__.py
│── tests/
│   └── test_organizer.py
│── requirements.txt
│── README.md
│── organizer.log (generated after run)
```

---

## 📝 Requirements

```
pytest
```

---

## 🔮 Future Enhancements

* YAML/JSON config for custom rules
* GUI version with drag & drop
* Watchdog mode (auto-organize new files)

---

## 👨‍💻 Author

Made with ❤️ by **Mudassir Ejaz**
