import random

# Datos actualizados de Provincia y Serie de cédula
datos_cedulas = [
    ("Distrito Nacional", "001"),
    ("Peravia", "003"),
    ("Monte Plata", "004"),
    ("Monte Plata", "005"),
    ("Monte Plata", "008"),
    ("Azua", "010"),
    ("San Juan", "011"),
    ("San Juan", "012"),
    ("San José de Ocoa", "013"),
    ("San Juan", "014"),
    ("Elías Piña", "015"),
    ("Elías Piña", "016"),
    ("Azua", "017"),
    ("Barahona", "018"),
    ("Barahona", "019"),
    ("Independencia", "020"),
    ("Barahona", "021"),
    ("Bahoruco", "022"),
    ("San Pedro de Macorís", "023"),
    ("El Seibo", "025"),
    ("La Romana", "026"),
    ("Hato Mayor", "027"),
    ("La Altagracia", "028"),
    ("El Seibo", "029"),
    ("Santiago", "031"),
    ("Valverde", "033"),
    ("Valverde", "034"),
    ("Santiago", "035"),
    ("Santiago", "036"),
    ("Puerto Plata", "037"),
    ("Puerto Plata", "038"),
    ("Puerto Plata", "039"),
    ("Puerto Plata", "040"),
    ("Monte Cristi", "041"),
    ("Dajabón", "043"),
    ("Dajabón", "044"),
    ("Monte Cristi", "045"),
    ("Santiago Rodríguez", "046"),
    ("La Vega", "047"),
    ("Monseñor Nouel", "048"),
    ("Sánchez Ramírez", "049"),
    ("La Vega", "050"),
    ("Sánchez Ramírez", "052"),
    ("La Vega", "053"),
    ("Espaillat", "054"),
    ("Duarte", "056"),
    ("Duarte", "057"),
    ("Duarte", "058"),
    ("Duarte", "059"),
    ("Espaillat", "061"),
    ("Espaillat", "065"),
    ("Duarte", "062"),
    ("Samaná", "065"),
    ("Pedernales", "069"),
    ("María Trinidad Sánchez", "071"),
    ("Dajabón", "073"),
    ("Elías Piña", "074"),
    ("Elías Piña", "075"),
    ("Independencia", "077"),
    ("Bahoruco", "076"),
    ("Bahoruco", "079"),
    ("Barahona", "080"),
    ("María Trinidad Sánchez", "081"),
    ("San Cristóbal", "083"),
    ("Peravia", "084"),
    ("La Altagracia", "085"),
    ("Espaillat", "088"),
    ("Monte Plata", "090"),
    ("Valverde", "092"),
    ("San Cristóbal", "093"),
    ("Santiago", "095"),
    ("Puerto Plata", "097"),
    ("Bahoruco", "098"),
    ("Hato Mayor", "100"),
    ("Monte Cristi", "101"),
    ("Puerto Plata", "102"),
    ("La Romana", "103"),
    ("San Cristóbal", "104"),
    ("San Cristóbal", "104"),
    ("San Cristóbal", "105"),
    ("Azua", "106"),
    ("Azua", "107"),
    ("San Juan", "108"),
    ("San Juan", "109"),
    ("Elías Piña", "110"),
    ("Bahoruco", "113"),
    ("Monte Cristi", "117"),
    ("San Pedro de Macorís", "402")
]

def generar_cedula():
    # Seleccionar aleatoriamente una entrada de datos de cédula
    provincia, serie = random.choice(datos_cedulas)
    
    # Generar el número de cédula aleatorio
    cedula = serie.zfill(3)  # Asegura que la serie tenga tres dígitos
    for _ in range(7):  # Genera los siguientes 7 dígitos
        cedula += str(random.randint(0, 9))
    
    # Calcular el dígito verificador
    suma = 0
    for i in range(len(cedula)):
        mod = 0
        if (i % 2) == 0:
            mod = 1
        else:
            mod = 2
        res = int(cedula[i]) * mod
        if res > 9:
            uno = res // 10
            dos = res % 10
            res = uno + dos
        suma += res
    digito_verificador = (10 - (suma % 10)) % 10
    cedula += str(digito_verificador)

    return cedula

if __name__ == "__main__":
    cedula_generada = generar_cedula()
    print("Cédula generada:", cedula_generada)
