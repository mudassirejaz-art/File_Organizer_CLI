import os
import shutil
import argparse
import logging
from datetime import datetime

# --- Logging Setup ---
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Helper Functions ---
def get_file_type(filename):
    """Return file type based on extension."""
    ext = os.path.splitext(filename)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        return "Images"
    elif ext in [".mp4", ".mkv", ".avi", ".mov"]:
        return "Videos"
    elif ext in [".mp3", ".wav", ".aac"]:
        return "Audio"
    elif ext in [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"]:
        return "Documents"
    elif ext in [".zip", ".rar", ".tar", ".gz"]:
        return "Archives"
    else:
        return "Others"


def organize_by_type(path, dry_run=False):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            folder = get_file_type(filename)
            target_dir = os.path.join(path, folder)

            if not dry_run:
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(target_dir, filename))

            logging.info(f"Moved {filename} → {folder}")
            print(f"[TYPE] {filename} → {folder}")


def organize_by_date(path, dry_run=False):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            timestamp = os.path.getctime(full_path)
            date_folder = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
            target_dir = os.path.join(path, date_folder)

            if not dry_run:
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(target_dir, filename))

            logging.info(f"Moved {filename} → {date_folder}")
            print(f"[DATE] {filename} → {date_folder}")


def organize_by_size(path, dry_run=False):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)

            if size < 1_000_000:  # <1MB
                size_folder = "Small_Files"
            elif size < 100_000_000:  # <100MB
                size_folder = "Medium_Files"
            else:
                size_folder = "Large_Files"

            target_dir = os.path.join(path, size_folder)

            if not dry_run:
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(target_dir, filename))

            logging.info(f"Moved {filename} → {size_folder}")
            print(f"[SIZE] {filename} → {size_folder}")


# --- Main CLI ---
def main():
    parser = argparse.ArgumentParser(description="Advanced File Organizer CLI")
    parser.add_argument("--path", required=True, help="Path to organize")
    parser.add_argument("--mode", required=True, choices=["type", "date", "size"], help="Organize mode")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without moving files")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(" Path does not exist!")
        return

    print(f"\n Organizing '{args.path}' by {args.mode}... (Dry Run: {args.dry_run})\n")

    if args.mode == "type":
        organize_by_type(args.path, args.dry_run)
    elif args.mode == "date":
        organize_by_date(args.path, args.dry_run)
    elif args.mode == "size":
        organize_by_size(args.path, args.dry_run)

    print("\n Organizing complete! Check organizer.log for details.")


if __name__ == "__main__":
    main()
