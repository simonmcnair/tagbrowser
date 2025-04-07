import sqlite3
import os

def create_db()
    if os.path.exists('photo_gallery.db'):
        print(f"Database photo_gallery.db already exists. Skipping creation.")
    else:
        print("Creating database and schema...")
        conn = sqlite3.connect('photo_gallery.db')
        cursor = conn.cursor()
    
        # Create table for photo tags
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            tag TEXT NOT NULL
        );
        ''')
    
        conn.commit()
        conn.close()
        print("Database and schema created successfully!")

if __name__ == '__main__':
    create_db()
