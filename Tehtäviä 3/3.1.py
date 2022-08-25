koko = float(input("Anna kuhan pituus senttimetreinä"))
if koko<=37:
    alle = 37 - koko
    print(f"Laske kuha takaisin. Kuha on {alle} senttiä liian pieni")
else:
    print(f"Kuha on tarpeeksi iso")