numeros=[]

print("Introduce 15 números enteros (entre 0 y 500):")
for i in range(15):
    while True:
        try:
            num = int(input(f"Posición [{i}]: "))
            if 0 <= num <= 500:
                numeros.append(num)
                break
            else:
                print("Error: El número debe estar comprendido entre 0 y 500.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
original=numeros.copy()

for i in range(len(numeros)):
    if numeros[i] % 5 != 0:
        numeros[i] = numeros[i] + (5 - (numeros[i] % 5))

print(f"\nArreglo original: {original}")
print(f"Array 'cincuerizado': {numeros}")