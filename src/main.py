from database import initialize_database
from watcher import start_watcher

def main():
    initialize_database()
    start_watcher()

if __name__ == "__main__":
    main()