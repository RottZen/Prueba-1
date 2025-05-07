
import random
print("HOLA, JUGUEMOS...")

while True:

    Menor = int(input("Ingrese un número"))
    Mayor = int(input("Ingrese un número mayor al anterior"))

    if Menor >= Mayor:
        print("Error, el segundo numero debe ser mayor al primero...")

    else: 
        break

print(f"Los numeros ingresados son {Menor} y {Mayor}")