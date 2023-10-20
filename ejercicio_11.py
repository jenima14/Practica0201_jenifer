Nom_Prod = input("Escribe el nombre del producto: ")
P_Uni = float(input("Escribe el precio unitario del producto: "))
Num_uds = int(input("Escribe el número de unidades: "))
costo_total = P_Uni * Num_uds
cadena_formateada = "{:s}: {:06.2f} - {:03d} - {:08.2f}".format(Nom_Prod, P_Uni, Num_uds, costo_total)
print(cadena_formateada)
input()