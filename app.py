from flask import Flask, render_template, request
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

    query = "SELECT generation, engine, start_of_production, body_type, seats, doors, acceleration, maximum_speed, power_to_weight_ratio, weight_to_torque_ratio, power, power_per_litre, engine_layout, engine_displacement, number_of_cylinders, engine_configuration, cylinder_bore, piston_stroke, number_of_valves_per_cylinder, engine_aspiration,fuel_tank_capacity, drive_wheel, number_of_gears_and_type_of_gearbox, fuel_consumption_combined, end_of_production  FROM porsche_9112"
    connection = create_connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )


    data_list = cursor.fetchall()
    print(data_list)

    return render_template('database.html', data=data_list)

@app.route('/search', methods=['GET', 'POST'])
def render_search_page():

    look_up = request.form['Search']
    title = "Search for: '" + look_up + "' "
    look_up = "%" + look_up + "%"

    query = ("SELECT generation, engine, start_of_production, body_type, seats, doors, acceleration, maximum_speed, power_to_weight_ratio, weight_to_torque_ratio, power, power_per_litre, engine_layout, engine_displacement, number_of_cylinders, engine_configuration, cylinder_bore, piston_stroke, number_of_valves_per_cylinder, engine_aspiration,fuel_tank_capacity, drive_wheel, number_of_gears_and_type_of_gearbox, fuel_consumption_combined, end_of_production FROM porsche_9112 WHERE generation LIKE ? OR engine LIKE ? OR start_of_production LIKE ? OR body_type LIKE ? OR seats LIKE ?  OR doors LIKE ? OR acceleration LIKE ? OR maximum_speed LIKE ? OR power_to_weight_ratio LIKE ? OR weight_to_torque_ratio LIKE ? OR power LIKE ? OR power_per_litre LIKE ? OR engine_layout LIKE ? OR engine_displacement LIKE ? OR number_of_cylinders LIKE ? OR engine_configuration LIKE ? OR cylinder_bore LIKE ? OR piston_stroke LIKE ? OR number_of_valves_per_cylinder LIKE ? OR engine_aspiration LIKE ? OR fuel_tank_capacity LIKE ? OR drive_wheel LIKE ? OR number_of_gears_and_type_of_gearbox LIKE ? OR fuel_consumption_combined LIKE ? OR end_of_production LIKE ?")
    connection = create_connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template("search.html", data=data_list)

@app.route('/gt3rs')
def render_gt3rs_page():
    gt3rs = "%" + "GT3 RS" + "%"

    query = ("SELECT generation, engine, start_of_production, body_type, seats, doors, acceleration, maximum_speed, power_to_weight_ratio, weight_to_torque_ratio, power, power_per_litre, engine_layout, engine_displacement, number_of_cylinders, engine_configuration, cylinder_bore, piston_stroke, number_of_valves_per_cylinder, engine_aspiration,fuel_tank_capacity, drive_wheel, number_of_gears_and_type_of_gearbox, fuel_consumption_combined, end_of_production FROM porsche_9112 WHERE generation LIKE ? OR engine LIKE ? OR start_of_production LIKE ? OR body_type LIKE ? OR seats LIKE ?  OR doors LIKE ? OR acceleration LIKE ? OR maximum_speed LIKE ? OR power_to_weight_ratio LIKE ? OR weight_to_torque_ratio LIKE ? OR power LIKE ? OR power_per_litre LIKE ? OR engine_layout LIKE ? OR engine_displacement LIKE ? OR number_of_cylinders LIKE ? OR engine_configuration LIKE ? OR cylinder_bore LIKE ? OR piston_stroke LIKE ? OR number_of_valves_per_cylinder LIKE ? OR engine_aspiration LIKE ? OR fuel_tank_capacity LIKE ? OR drive_wheel LIKE ? OR number_of_gears_and_type_of_gearbox LIKE ? OR fuel_consumption_combined LIKE ? OR end_of_production LIKE ?")
    connection = create_connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs,  gt3rs))

    data_list = cursor.fetchall()

    return render_template("gt3rs.html", data=data_list)

@app.route('/dakar', methods=['GET', 'POST'])
def render_dakar_page():

    look_up = "%"+ "dakar" + "%"

    query = ("SELECT generation, engine, start_of_production, body_type, seats, doors, acceleration, maximum_speed, power_to_weight_ratio, weight_to_torque_ratio, power, power_per_litre, engine_layout, engine_displacement, number_of_cylinders, engine_configuration, cylinder_bore, piston_stroke, number_of_valves_per_cylinder, engine_aspiration,fuel_tank_capacity, drive_wheel, number_of_gears_and_type_of_gearbox, fuel_consumption_combined, end_of_production FROM porsche_9112 WHERE generation LIKE ? OR engine LIKE ? OR start_of_production LIKE ? OR body_type LIKE ? OR seats LIKE ?  OR doors LIKE ? OR acceleration LIKE ? OR maximum_speed LIKE ? OR power_to_weight_ratio LIKE ? OR weight_to_torque_ratio LIKE ? OR power LIKE ? OR power_per_litre LIKE ? OR engine_layout LIKE ? OR engine_displacement LIKE ? OR number_of_cylinders LIKE ? OR engine_configuration LIKE ? OR cylinder_bore LIKE ? OR piston_stroke LIKE ? OR number_of_valves_per_cylinder LIKE ? OR engine_aspiration LIKE ? OR fuel_tank_capacity LIKE ? OR drive_wheel LIKE ? OR number_of_gears_and_type_of_gearbox LIKE ? OR fuel_consumption_combined LIKE ? OR end_of_production LIKE ?")
    connection = create_connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up, look_up))

    data_list = cursor.fetchall()

    return render_template("dakar.html", data=data_list)

if __name__ == '__main__':
    app.run()