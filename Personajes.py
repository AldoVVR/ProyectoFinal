# Definimos la clase Personaje
import random


class Individuo:
    def __init__(self, name, level, health, attack, defense, items=[]):
        
        #Constructor de la clase Enemigo. Crea un objeto Enemigo con un nombre,
        #nivel, salud, ataque, defensa y una lista de objetos.
        
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.items = items
    
    def receive_damage(self, player):
        
        #Metodo que recibe el dano causado por el oponente.
        
        damage_received = max(0, player.attack - self.defense)
        self.health -= damage_received
        print(f"{player.name} attacked {self.name} and caused {damage_received} points of damage.")
    
    def is_alive(self):
        
        #Metodo que comprueba si el enemigo esta vivo.
        
        return self.health > 0
    
    def perform_attack(self, target):

        #Metodo que realiza el ataque al enemigo.
        
        damage_caused = self.attack
        if random.randint(1, 6) == 6:
            print("Critical hit!")
            damage_caused *= 2
        target.health -= damage_caused
        print(f"{self.name} attacked {target.name} and caused {damage_caused} points of damage.")
    
class Personaje(Individuo):
    def __init__(self, name, level, health, attack, defense, items=[]):
        
        super().__init__(name, level, health, attack, defense, items)
        
    
    def use_item(self, item):
        
        #Metodo que utiliza un objeto.
        
        if item["tipo"] == "cura":
            self.health += item["efecto"]
            print(f"{self.name} used {item['nombre']} and restored {item['efecto']} health points.")
        elif item["tipo"] == "potenciador":
            self.attack += item["efecto"]
            print(f"{self.name} used {item['nombre']} and increased their attack by {item['efecto']} points.")
        elif item["tipo"] == "escudo":
            self.defense += item["efecto"]
            print(f"{self.name} used {item['nombre']} and increased their defense by {item['efecto']} points.")


# Definimos la clase Enemigo
class Enemigo(Individuo):
    
    def __init__(self, name, level, health, attack, defense, items=[]):
        
        super().__init__(name, level, health, attack, defense, items)
    
    def receive_damage(self, player):
        
        #Metodo que recibe el dano causado por el oponente.
        #Si sacando un numero del 1 al 6 el enemigo saca un 6, reduce 20% el dano recibido
        if random.randint(1, 6) == 6:
            damage_received *= 0.8
        damage_received = max(0, player.attack - self.defense)
        self.health -= damage_received
        print(f"{player.name} attacked {self.name} and caused {damage_received} points of damage.")
        
