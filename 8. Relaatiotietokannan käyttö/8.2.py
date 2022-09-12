import mysql.connector

#Etsii maan lentokenttien tyypit
def search(country):
    sql = "SELECT type FROM airport WHERE iso_country=\"" + country + "\""
    cursor = connection.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    return outcome

#Laskee lentokenttä tyyppien määrän
def count(list):
    l = {}
    for i in list:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    return l

#Nätimpää printtausta varten
def printing(list):
    for i in list:
        print(i, list[i])

connection = mysql.connector.connect(
    host= "localhost",
    port= 3306,
    database= "flight_game",
    user= "dbuser",
    password= "hunter2",
    autocommit= True
)

userInput = input("Anna maakoodi")
a = search(userInput)
b = count(a)
printing(b)