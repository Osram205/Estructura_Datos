while True:
    cola = []
    
    while True:
        print("\n--- MENÚ COLA ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            try:
                numero = int(input("Ingresa un número para la cola: "))
                cola.append(numero)
                print(f"Se agregó el número {numero} a la cola.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        elif opcion == "2":
            if len(cola) == 0:
                print("La cola está vacía, no hay elementos para borrar.")
            else:
                eliminado = cola.pop(0)
                print(f"Se eliminó el primer elemento: {eliminado}")
        elif opcion == "3":
            if len(cola) == 0:
                print("La cola está vacía.")
            else:
                print("Elementos de la cola:")
                for elem in cola:
                    print(elem)
                print("Cola actual:", cola)
        elif opcion == "4":
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            
    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
    if repetir != "s" and repetir != "si":
        print("Programa finalizado.")
        break
