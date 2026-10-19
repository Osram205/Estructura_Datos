while True:
    pila = []
    
    while True:
        print("\n--- MENÚ PILA ---")
        print("1. Insertar pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            try:
                numero = int(input("Ingresa un número para la pila: "))
                pila.append(numero)
                print(f"Se agregó el número {numero} a la pila.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        elif opcion == "2":
            if len(pila) == 0:
                print("La pila está vacía, no hay elementos para borrar.")
            else:
                eliminado = pila.pop()
                print(f"Se quitó el último elemento de la pila: {eliminado}")
        elif opcion == "3":
            if len(pila) == 0:
                print("La pila está vacía.")
            else:
                print("Elementos de la pila:")
                for elem in pila:
                    print(elem)
                print("Pila actual:", pila)
        elif opcion == "4":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            
    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
    if repetir != "s" and repetir != "si":
        print("Programa finalizado.")
        break
