import os
import shutil

# Folder to organize
folder = r"D:\Download"

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
    "Code": [".py", ".html", ".css", ".js", ".java", ".cpp", ".c"]
}

# Create folders
for category in categories:
    path = os.path.join(folder, category)
    os.makedirs(path, exist_ok=True)

# Sort files
for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    # Ignore folders
    if not os.path.isfile(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(filename)[1].lower()

    moved = False

    # Find category
    for category, extensions in categories.items():
        if extension in extensions:

            destination = os.path.join(folder, category, filename)
            shutil.move(file_path, destination)

            print(f"Moved: {filename} → {category}")
            moved = True
            break

    # Files that don't match any category
    if not moved:
        destination = os.path.join(folder, "Others", filename)
        os.makedirs(destination.rsplit("\\", 1)[0], exist_ok=True)
        shutil.move(file_path, destination)

        print(f"Moved: {filename} → Others")

print("\n✅ File sorting completed!")