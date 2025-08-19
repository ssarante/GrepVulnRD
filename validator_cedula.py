import sys
import re

def validar_cedula(ced):
    """ Valida el documento de identidad oficial de la Republica Dominicana"""
    # Validates the official identity document of the Dominican Republic 
    try:
        # Solo se aceptan digitos

        regex = re.compile(r'\d+')
        c = filter(regex.search, ced)
        cedula = c[0:len(c) - 1]
        verificador = c[-1:]
        suma = 0
        if len(c) != 11:
            return False

        for i in range(len(cedula)):
            mod = 0
            if (i % 2) == 0:
                mod = 1
            else:
                mod = 2
            res = str(int(cedula[i]) * mod) 
            if int(res) > 9:
                res = str(res)
                uno = res[0:1]
                dos = res[1:2] 
                res = int(uno) + int(dos)

            if res:
                suma += int(res)
               

        el_numero = (10 - (suma % 10)) % 10
        if str(el_numero) == verificador and cedula[:3] != "000":
            print("La Cedula es valida")
            return True

        else:
            print("La Cedula es incorrecta")
            return False

    except ValueError:
        print("Numero de cedula con datos erroneos, por favor solo se aceptan guion y numeros")
        return False

if __name__ == "__main__":
    validar_cedula(sys.argv[1])
    