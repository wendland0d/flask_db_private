from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__, template_folder='templates')


def db_connection(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = db_connection('data.sqlite')
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return render_template('index.html', posts=posts)


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    print(search_query)
    conn = db_connection('data.sqlite')
    posts = conn.execute(f'SELECT * FROM posts WHERE text LIKE "%{search_query}%" '
                         f'ORDER BY created_date DESC LIMIT 20').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/deleted', methods=['POST'])
def delete():
    pass


if __name__ == "__main__":
    app.run()
