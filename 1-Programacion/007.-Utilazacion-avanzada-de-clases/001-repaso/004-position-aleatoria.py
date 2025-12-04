# Non Playable Character
import random

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personaje1 = Npc(4,3)
personaje2 = Npc(5,4)

personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
    xaleatoria = random.randint(0,500)
    yaleatoria = random.randint(0,500)
    personajes.append(Npc(xaleatoria,yaleatoria))


print(personajes)