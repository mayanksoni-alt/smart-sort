import time 
from pathlib import Path
from organizer import sort_file
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
        def on_created(self, event):
            
            if event.is_directory:
                return

            sort_file(Path(event.src_path))



def start_watcher():
    
    downloads = Path.home() / "Downloads"
    observer = Observer()
    observer.schedule(MyHandler(), str(downloads), recursive=False) 
    observer.start()

    print(f"👀 Watching: {downloads}")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()