import math
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.
# math.floor

leiviska_paino = 20 * 32 * 13.3
naula_paino = 32 * 13.3
luoti_paino = 13.3

leiviska_maara = float(input("Anna leiviskat"))
naula_maara = float(input("Anna naulat"))
luoti_maara = float(input("anna luodit"))

massa_yht = (leiviska_maara * leiviska_paino) + (naula_maara * naula_paino) + (luoti_maara * luoti_paino)

massa_kg = math.floor(massa_yht / 1000)

massa_gramma = massa_yht - (massa_kg * 1000)

print(f" Massa nykymittojen mukaan:\n{massa_kg} kilogrammaa ja {massa_gramma:.2f} grammaa.")