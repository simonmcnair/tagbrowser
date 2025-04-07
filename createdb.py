import sqlite3

def create_db():
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

if __name__ == '__main__':
    create_db()
