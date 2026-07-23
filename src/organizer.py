from pathlib import Path
import shutil 
import hashlib

from rules import get_category
from logger import log_file
from database import record_file_move

IGNORE_EXTENSIONS = {
    ".crdownload",
    ".download",
    ".tmp",
    ".part",
}

downloads = Path.home() / "Downloads"


def get_file_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()

def create_folder(category):

    destination = downloads / category
    destination.mkdir(exist_ok=True)
    return destination


def move_file(file, destination):
    new_path = destination / file.name

    if new_path.exists():
        if (
            file.stat().st_size == new_path.stat().st_size
            and get_file_hash(file) == get_file_hash(new_path)
        ):
            print(f"⚠️ Duplicate file: {file.name}")
            file.unlink()
            return None

        counter = 1

        while new_path.exists():
            new_path = destination / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

    shutil.move(file, new_path)
    return new_path

def sort_file(file):

    if not file.exists():
        return

    if file.name.startswith("."):
        return
    
    if file.suffix in IGNORE_EXTENSIONS:
        return


    category = get_category(file)
    organize_file(file, category)
    
    
    
def organize_file(file, category):
    old_path = str(file)
    file_name = file.name
    extension = file.suffix.lower()

    destination = create_folder(category)
    new_path = move_file(file, destination)

    if new_path is None:
        return

    record_file_move(
        file_name=file_name,
        extension=extension,
        old_path=old_path,
        new_path=new_path,
        category=category,
    )

    log_file(new_path, category)