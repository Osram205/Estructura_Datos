"""
================================================================================
Universidad Politécnica de Querétaro
Materia: Estructura de Datos
Alumno: Osman Kenneth Ramírez Trejo
Profesor: Ing. Alejandra Briones Patiño
Fecha: 19 de octubre de 2026

Ejercicio 1: Implementación de Cola (Queue - FIFO) con Menú Interactivo
================================================================================
Descripción:
Este programa administra una estructura de datos de tipo Cola (First In, First Out)
mediante un menú iterativo basado en ciclos `while` y `for`. Permite insertar
elementos numéricos, eliminar el primer elemento ingresado, visualizar los
elementos actuales y salir. Al salir del menú, pregunta al usuario si desea
ejecutar nuevamente el programa completo.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

def ejecutar_cola():
    while True:
        cola = []
        print("\n" + "=" * 45)
        print("     SISTEMA DE GESTIÓN DE COLA (FIFO)")
        print("=" * 45)
        
        while True:
            print("\n" + "-" * 35)
            print("             MENÚ COLA")
            print("-" * 35)
            print("1. Insertar cola")
            print("2. Borrar en cola")
            print("3. Listar cola")
            print("4. Salir")
            print("-" * 35)
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                # Opción 1: Insertar cola (Enqueue)
                # Validamos que el usuario ingrese un número válido
                valido = False
                while not valido:
                    entrada = input("\nIngrese el número a insertar en la cola: ").strip()
                    try:
                        numero = int(entrada)
                        cola.append(numero)
                        print(f"-> Éxito: Se insertó el número {numero} al final de la cola.")
                        valido = True
                    except ValueError:
                        print("-> Error: Ingrese un valor numérico entero válido.")
            
            elif opcion == "2":
                # Opción 2: Borrar en cola (Dequeue)
                # En una cola se retira el primer elemento que entró (índice 0)
                if len(cola) == 0:
                    print("\n-> Aviso: La cola está vacía. No hay elementos para borrar.")
                else:
                    elemento_eliminado = cola.pop(0)
                    print(f"\n-> Éxito: Se eliminó el primer elemento de la cola: {elemento_eliminado}")
            
            elif opcion == "3":
                # Opción 3: Listar cola
                # Mostramos los elementos en orden de llegada utilizando un ciclo for
                if len(cola) == 0:
                    print("\n-> La cola se encuentra actualmente vacía.")
                else:
                    print(f"\n--- Contenido de la Cola ({len(cola)} elementos) ---")
                    print("FRENTE -> ", end="")
                    for i, elem in enumerate(cola):
                        if i < len(cola) - 1:
                            print(f"[{elem}] -> ", end="")
                        else:
                            print(f"[{elem}]", end="")
                    print(" <- FINAL")
                    print(f"Representación en lista: {cola}")
            
            elif opcion == "4":
                # Opción 4: Salir del menú de la cola
                print("\nSaliendo del menú de la cola...")
                break
            
            else:
                print("\n-> Opción no válida. Por favor, seleccione un número entre 1 y 4.")
        
        # Pregunta obligatoria según especificaciones del ejercicio:
        # "¿Desea ejecutar nuevamente el programa?"
        while True:
            respuesta = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").strip().lower()
            if respuesta in ["s", "si", "sí"]:
                print("\nReiniciando el programa de Cola...")
                break
            elif respuesta in ["n", "no"]:
                print("\n¡Gracias por utilizar el programa de Colas! Hasta luego.")
                return
            else:
                print("Por favor, responda con 's' (sí) o 'n' (no).")

if __name__ == "__main__":
    ejecutar_cola()
