fecha_nac = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, año = fecha_nac.split('/')
if len(dia) == 1:
    dia = "0" + dia
if len(mes) == 1:
    mes = "0" + mes
print("Día: ", dia)
print("Mes: ", mes)
print("Año: ", año)
input()