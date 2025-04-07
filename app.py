from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('photo_gallery.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route to display the gallery
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get all photos and their tags
    cursor.execute('''
    SELECT DISTINCT filename FROM tags;
    ''')
    photos = cursor.fetchall()

    photo_tags = {}
    for photo in photos:
        cursor.execute('''
        SELECT tag FROM tags WHERE filename = ?;
        ''', (photo['filename'],))
        tags = [row['tag'] for row in cursor.fetchall()]
        photo_tags[photo['filename']] = tags

    conn.close()

    return render_template('index.html', photo_tags=photo_tags)

# Route to add a tag
@app.route('/add_tag/<filename>', methods=['POST'])
def add_tag(filename):
    tag = request.form['tag']
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert the new tag into the database
    cursor.execute('''
    INSERT INTO tags (filename, tag) VALUES (?, ?);
    ''', (filename, tag))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Route to remove a tag
@app.route('/remove_tag/<filename>/<tag>', methods=['GET'])
def remove_tag(filename, tag):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Remove the tag from the database
    cursor.execute('''
    DELETE FROM tags WHERE filename = ? AND tag = ?;
    ''', (filename, tag))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
