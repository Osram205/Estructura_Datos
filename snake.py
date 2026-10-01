import os, time, msvcrt, sys

# Imprimir emojis en Windows
sys.stdout.reconfigure(encoding='utf-8')

# 1. Creamos matriz (Tablero)
filas = 10
columnas = 15
tablero = [["⬛" for _ in range(columnas)] for _ in range(filas)]

# 2. Agregamos elementos iniciales
y, x = 5, 5
tablero[y][x] = "🟩" # Cabeza
tablero[3][10] = "🍎" # Comida

# Lista de coordenadas (Cuerpo)
cuerpo = [(y, x)]
dir_y, dir_x = 0, 1

# Bucle infinito (Juego)
while True:
    os.system("cls") # Limpiamos consola
    
    # Imprimimos la matriz actual
    for fila in tablero:
        print("".join(fila))
        
    print("\nControles: W (Arriba), S (Abajo), A (Izq), D (Der)")
        
    # Leer teclado sin pausar
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode('utf-8', 'ignore').lower()
        if tecla == 'w' and dir_y == 0: dir_y, dir_x = -1, 0
        if tecla == 's' and dir_y == 0: dir_y, dir_x = 1, 0
        if tecla == 'a' and dir_x == 0: dir_y, dir_x = 0, -1
        if tecla == 'd' and dir_x == 0: dir_y, dir_x = 0, 1
        if tecla == 'q': break
        
    # Nueva posición de cabeza
    y += dir_y
    x += dir_x
    
    # ¿Chocó con la pared?
    if y < 0 or y >= filas or x < 0 or x >= columnas:
        print("¡Chocaste! Game Over.")
        break
        
    # 3. Insertamos nueva cabeza
    cuerpo.insert(0, (y, x))
    
    # Lógica de comer y avanzar
    if tablero[y][x] == "🍎":
        # Creció, no borramos cola
        tablero[y][x] = "🟩"
        # Comida en lugar fijo (ejemplo)
        tablero[8][2] = "🍎" 
    else:
        # Avanza, borramos la cola
        tablero[y][x] = "🟩"
        
        # 4. Eliminamos la cola
        cola_y, cola_x = cuerpo.pop()
        tablero[cola_y][cola_x] = "⬛"

    # Velocidad del juego
    time.sleep(0.15)
