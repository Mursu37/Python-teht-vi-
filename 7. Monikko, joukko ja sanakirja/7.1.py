kuukaudet = ("tammikuu", "helmikuu", "maaliskuu",
             "huhtikuu", "toukokuu","kesäkuu",
             "heinäkuu", "elokuu", "syyskuu",
             "lokakuu", "marraskuu", "joulukuu")
jarjestysluku = int(input("Anna kuukauden numero"))
kuukausi = jarjestysluku - 1
if kuukausi < 2 or kuukausi == 11:
    print("talvi")
elif kuukausi < 5:
    print("kevät")
elif kuukausi < 8:
    print("kesä")
elif kuukausi < 11:
    print("syksy")