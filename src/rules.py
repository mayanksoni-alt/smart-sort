from config import config


def get_category(file):

    extension = file.suffix.lower()
    category = config["categories"].get(extension, "Others")
    return category
