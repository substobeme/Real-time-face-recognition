from flask import Flask, render_template
import mysql.connector
import base64

DB = Flask(__name__)

@DB.route('/')
def index():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#12#ASUS#SUBS#1",
        database="face_info"
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT ID, Name, Time, Photo FROM face")
    records = cursor.fetchall()
    cursor.close()
    db_connection.close()


    for i in range(len(records)):
        records[i] = list(records[i])
        records[i][3] = base64.b64encode(records[i][3]).decode('utf-8')

    return render_template('design.html', records=records)

if __name__ == '__main__':
    DB.run(debug=True)