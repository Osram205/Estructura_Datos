"""
================================================================================
Universidad Politécnica de Querétaro
Materia: Estructura de Datos
Alumno: Osman Kenneth Ramírez Trejo
Profesor: Ing. Alejandra Briones Patiño
Fecha: 19 de octubre de 2026

Ejercicio 2: Implementación de Pila (Stack - LIFO) con Menú Interactivo
================================================================================
Descripción:
Este programa administra una estructura de datos de tipo Pila (Last In, First Out)
mediante un menú interactivo implementado con ciclos `while` y `for`. Permite
apilar (push) elementos numéricos solicitados al usuario, desapilar (pop) el
último elemento ingresado, visualizar el estado actual de la pila y salir.
Al salir, consulta al usuario si desea reiniciar la ejecución del programa.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def ejecutar_pila():
    while True:
        pila = []
        print("\n" + "=" * 45)
        print("     SISTEMA DE GESTIÓN DE PILA (LIFO)")
        print("=" * 45)
        
        while True:
            print("\n" + "-" * 35)
            print("             MENÚ PILA")
            print("-" * 35)
            print("1. Insertar pila (Push)")
            print("2. Borrar en pila (Pop)")
            print("3. Listar pila")
            print("4. Salir")
            print("-" * 35)
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                # Opción 1: Insertar pila (Push)
                # Validamos que la entrada sea un número entero
                valido = False
                while not valido:
                    entrada = input("\nIngrese el número a agregar a la pila: ").strip()
                    try:
                        numero = int(entrada)
                        pila.append(numero)
                        print(f"-> Éxito: Se agregó el número {numero} en el tope de la pila.")
                        valido = True
                    except ValueError:
                        print("-> Error: Debe ingresar un valor numérico entero.")
            
            elif opcion == "2":
                # Opción 2: Borrar en pila (Pop)
                # En una pila (LIFO) se remueve el último elemento ingresado (el tope)
                if len(pila) == 0:
                    print("\n-> Aviso: La pila está vacía. No hay elementos para desapilar.")
                else:
                    elemento_desapilado = pila.pop()
                    print(f"\n-> Éxito: Se desapiló el elemento en el tope de la pila: {elemento_desapilado}")
            
            elif opcion == "3":
                # Opción 3: Listar pila
                # Mostramos la estructura verticalmente desde el TOPE hacia la BASE
                if len(pila) == 0:
                    print("\n-> La pila se encuentra actualmente vacía.")
                else:
                    print(f"\n--- Contenido de la Pila ({len(pila)} elementos) ---")
                    print("  [TOPE / CIMA]")
                    # Recorremos en orden inverso utilizando un ciclo for con reversed()
                    for idx, elem in enumerate(reversed(pila)):
                        pos_real = len(pila) - 1 - idx
                        flecha = " <--- Tope" if idx == 0 else ""
                        print(f"  | {elem:^7} | (Posición {pos_real}){flecha}")
                    print("  +---------+")
                    print("  [  BASE  ]")
                    print(f"Representación en lista estándar: {pila}")
            
            elif opcion == "4":
                # Opción 4: Salir del menú de la pila
                print("\nSaliendo del menú de la pila...")
                break
            
            else:
                print("\n-> Opción no válida. Por favor, seleccione un número entre 1 y 4.")
        
        # Pregunta obligatoria según especificaciones del ejercicio:
        # "¿Desea ejecutar nuevamente el programa?"
        while True:
            respuesta = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").strip().lower()
            if respuesta in ["s", "si", "sí"]:
                print("\nReiniciando el programa de Pila...")
                break
            elif respuesta in ["n", "no"]:
                print("\n¡Gracias por utilizar el programa de Pilas! Hasta luego.")
                return
            else:
                print("Por favor, responda con 's' (sí) o 'n' (no).")

if __name__ == "__main__":
    ejecutar_pila()
