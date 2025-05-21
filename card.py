
class Card:
    def __init__(self, attack=0, health=1, pattern=('------','------','------')):
        self.attack = attack
        self.health = health
        self.pattern = pattern

    def __str__(self):
        return f'''  ______  
 |{self.pattern[0]}| 
 |{self.pattern[1]}| 
 |------| 
 | {self.attack}  {self.health} | 
 |______| 
          
 '''
    