C_compra = input("Escribe los productos de la cesta de compra: ")
Productos = C_compra.split(",")
print(*Productos, sep='\n')
input()