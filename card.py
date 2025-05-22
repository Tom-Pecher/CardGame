
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
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_pattern(self):
        return self.pattern
    
    def change_health(self, delta):
        self.health += delta