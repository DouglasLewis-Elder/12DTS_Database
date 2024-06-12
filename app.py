from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def render_index_page():
    return render_template('index.html')

@app.route('/database')

def render_database_page():
    return render_template('database.html')

if __name__ == '__main__':
    app.run()
