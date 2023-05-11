import random
from Personajes import Personaje, Enemigo
#from pdb import set_trace; set_trace()

# Definimos la funcion para mostrar las opciones del jugador
def mostrar_opciones():
    print("1. Atacar")
    print("2. Usar objeto")

# Definimos la funcion para que el jugador seleccione una opcion
def seleccionar_opcion():
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Selecciona una opcion: "))
            if opcion < 1 or opcion > 2:
                print("Opcion invalida, por favor selecciona una opcion del 1 al 2.")
            else:
                opcion_valida = True
        except ValueError:
            print("Opcion invalida, por favor selecciona una opcion del 1 al 2.")
    return opcion

# Definimos la funcion para que el jugador seleccione un objeto
def seleccionar_objeto(player):
    objeto_valido = False
    while not objeto_valido:
        try:
            objeto_seleccionado = int(input("Selecciona un objeto (1-3): "))
            if objeto_seleccionado < 1 or objeto_seleccionado > 3:
                print("Objeto invalido, por favor selecciona un objeto del 1 al 3.")
            elif len(player.items) == 0:
                print("No tienes objetos en tu inventario.")
                objeto_valido = True
            elif objeto_seleccionado > len(player.items):
                print("No tienes un objeto en esa posicion.")
            else:
                objeto_valido = True
        except ValueError:
            print("Objeto invalido, por favor selecciona un objeto del 1 al 3.")
    return objeto_seleccionado - 1

# Definimos la funcion para la batalla
def batalla(player, enemies):
    print("Comienza la batalla!")
    enemigo = random.choice(enemies)
    print(f"Te enfrentaras a {enemigo.name}.")

    while player.is_alive() and enemigo.is_alive():
        enemies_defeated = 0
        print(f"\n{player.name}: {player.health} HP | {enemigo.name}: {enemigo.health} HP")
        mostrar_opciones()
        opcion_seleccionada = seleccionar_opcion()
        if opcion_seleccionada == 1:
            player.attack(enemigo)

            if enemigo.is_alive():
                enemigo.attack(player)

            if not enemigo.is_alive():
                print(f"{enemigo.name} ha sido derrotado.")
                enemies_defeated = enemies_defeated + 1
                break
            enemigo.receive_damage(player)
            if not player.is_alive():
                print(f"{player.name} ha sido derrotado.")
                break
        elif opcion_seleccionada == 2:
            objeto_seleccionado = seleccionar_objeto(player)
            objeto = player.items[objeto_seleccionado]
            player.use_item(objeto)
            del player.items[objeto_seleccionado]
            enemigo.receive_damage(player)
            
            if enemigo.is_alive():
                enemigo.attack(player)
                
            if not player.is_alive():
                print(f"{player.name} ha sido derrotado.")
                break
            
    print("Fin de la batalla.")
    print(f"Defeated enemies: {enemies_defeated}")

# Creamos los personajes

player = Personaje("Omagical", 1, 100, 10, 5, [])
enemies = [
    Enemigo(
        "Shadow",
        1,
        55,
        10,
        5,
        [
            {"nombre": "Pocion de curacion", "tipo": "cura", "efecto": 20},
            {"nombre": "Pocion de fuerza", "tipo": "potenciador", "efecto": 5},
            {"nombre": "Escudo magico I", "tipo": "escudo", "efecto": 5}
        ]
    ),
    Enemigo("Ghost Shadow", 2, 65, 12, 7, [
    {"nombre": "Pocion de curacion", "tipo": "cura", "efecto": 20},
    {"nombre": "Pocion de fuerza", "tipo": "potenciador", "efecto": 5},
    {"nombre": "Escudo magico II", "tipo": "escudo", "efecto": 10},
    ]),
    Enemigo("Shadow Knight", 3, 85, 14, 10, [
    {"nombre": "Pocion de curacion", "tipo": "cura", "efecto": 20},
    {"nombre": "Pocion de fuerza", "tipo": "potenciador", "efecto": 5},
    {"nombre": "Escudo magico III", "tipo": "escudo", "efecto": 15},
    ]),
    Enemigo("Shadow Dragon", 4, 105, 16, 15, [
    {"nombre": "Pocion de curacion", "tipo": "cura", "efecto": 20},
    {"nombre": "Pocion de fuerza", "tipo": "potenciador", "efecto": 5},
    {"nombre": "Escudo magico IV", "tipo": "escudo", "efecto": 20},
    ])
]

batalla(player, enemies)
