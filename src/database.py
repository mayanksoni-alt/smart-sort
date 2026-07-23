from pathlib import Path
import sqlite3

# Project root
BASE_DIR = Path(__file__).parent.parent

# Database folder
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

# Database file
DB_PATH = DATABASE_DIR / "smart_sort.db"


def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT NOT NULL,
        extension TEXT,
        old_path TEXT,
        new_path TEXT,
        category TEXT,
        moved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
    
def record_file_move(file_name, extension, old_path, new_path, category):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO history (
                file_name,
                extension,
                old_path,
                new_path,
                category
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                file_name,
                extension,
                str(old_path),
                str(new_path),
                category,
            ),
        )

        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()