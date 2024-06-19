from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "webtags.db"

def create_connect(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection
    except Error as e:
        print(e)
        return None


@app.route('/')
def render_index_page():
    return render_template('index.html')


@app.route('/database')
def render_database_page():

    query = "SELECT generation, engine, start_of_production, body_type, seats, doors, acceleration, maximum_speed, power_to_weight_ratio, weight_to_torque_ratio, power, power_per_litre, torque, engine_layout, engine_displacement FROM porsche_9112"
    connection = create_connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('database.html', data=data_list)


if __name__ == '__main__':
    app.run()