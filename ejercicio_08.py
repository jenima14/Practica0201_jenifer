precio_euros = float(input("Ingresa el precio en euros (con dos decimales): "))
euros = int(precio_euros)
centimos = int((precio_euros - euros) * 100)
print("El precio es:", euros, "euros y", centimos, "céntimos")
input()