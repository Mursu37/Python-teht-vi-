months = ("tammikuu", "helmikuu", "maaliskuu",
             "huhtikuu", "toukokuu","kesäkuu",
             "heinäkuu", "elokuu", "syyskuu",
             "lokakuu", "marraskuu", "joulukuu")
userInput = int(input("Anna kuukauden numero"))
month = userInput - 1
print(months[month])
if month < 2 or month == 11:
    print("talvi")
elif month < 5:
    print("kevät")
elif month < 8:
    print("kesä")
elif month < 11:
    print("syksy")