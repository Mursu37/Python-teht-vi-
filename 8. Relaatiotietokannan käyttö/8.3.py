from geopy import distance
import mysql.connector
def fetch_data(ap):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=\"" + ap + "\""
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    return outcome

def calculate_distance(ap1, ap2):
    return (distance.distance(ap1, ap2).km)

connection = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    database= "flight_game",
    user= "dbuser",
    password= "hunter2",
    autocommit= True
)

userInput = input("Anna ensimmäisen lentokentän ICAO koodi")
airport1 = fetch_data(userInput)
userInput2 = input("Anna toisen lentokentän ICAO koodi")
airport2 = fetch_data(userInput2)

distance = calculate_distance(airport1, airport2)

print(f"Lentokenttien välinen etäisyys on {round(distance,2)}km")