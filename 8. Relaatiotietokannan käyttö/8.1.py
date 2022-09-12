import mysql.connector
def search(code):
    sql = "SELECT name, municipality FROM airport WHERE ident=\"" + code + "\""
    cursor = connection.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    for i in outcome:
        print(f'Lentokenttä on "{i[0]}" \nSijaintikunta on "{i[1]}"')

connection = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    database= "flight_game",
    user= "dbuser",
    password= "hunter2",
    autocommit= True
)

ICAO = input("Anna ICAO koodi")
search(ICAO)