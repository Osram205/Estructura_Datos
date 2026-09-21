def main():
    array = []
    
    print("--- Ingreso de datos ---")
    print("Por favor, ingresa 10 números enteros para llenar el arreglo.")
    
    for i in range(1, 11):
        while True:
            try:
                valor_str = input(f"Ingresa el número para la posición {i}: ")
                valor = int(valor_str)
                array.append(valor)
                break 
            except ValueError:
                print("Error: Por favor ingresa un número entero válido.")

    original = array.copy()

    print(f"Arreglo inicial: {array}")

    posicion = 0
    nuevo = 0

    while True:
        try:
            posicion_str = input("\nIngrese la posicion a modificar (1 al 10): ")
            posicion = int(posicion_str)

            if 1 <= posicion <= 10:
                break
            else:
                print("Error: Posicion fuera de rango, ingrese un numero del 1 al 10")
        except ValueError:
            print("Error: ingrese un numero entero valido")

    while True:
        try:
            nuevo_str = input(f"Ingrese el nuevo valor para la posicion {posicion}: ")
            nuevo = int(nuevo_str)
            break
        except ValueError:
            print("Error: Favor de ingresar un numero entero valido")

    array[posicion] = nuevo

    print("\n-----Resultado-----")
    print(f"Arreglo original: {original}")
    print(f"Arreglo Modificado: {array}")

if __name__ == "__main__":
    main()