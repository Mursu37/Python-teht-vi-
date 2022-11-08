import mysql.connector
from flask import Flask
app = Flask("__name__")


@app.route("/kenttä/<icao>")
def fetch_data(icao):
    try:
        sql = f'SELECT name, municipality FROM airport WHERE IDENT="{icao}"'
        print(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)
        name = data[0]
        municipality = data[1]
        answer = {
            "Name": name,
            "Municipality": municipality
        }
        return answer
    except TypeError:
        return f"Airport \"{icao}\" not in database"


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="dbuser",
    password="hunter2",
    autocommit=True
)

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
