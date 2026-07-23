FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".mp4": "Videos",
    ".mov": "Videos",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".pdf": "PDFs",

    ".zip": "Archives",
    ".rar": "Archives",

    ".docx": "Documents",
    ".txt": "Documents",
    ".pages": "Documents",
}


def get_category(file):
    
    extension = file.suffix.lower()
    category = FILE_TYPES.get(extension, "Others")
    return category
