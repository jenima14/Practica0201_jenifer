correo_actual = input("Ingresa tu correo electrónico: ")
Usuario = correo_actual.split('@')[0]
nuevo_correo = "{}@ceu.es".format(Usuario)
print("Tu nuevo correo electrónico es:", nuevo_correo)
input()