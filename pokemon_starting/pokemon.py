
class Pokemon:
    def __init__(self, name, level, poke_type):
        self.name = name
        self.level = level
        self.type = poke_type
        self.max_health = level * 3
        self.current_health = level * 3
        self.knocked_out = False
        self.experience = 0
        self.base_level = level
    
    def __repr__(self):
        return str((self.name, str(self.level), self.type, str(self.max_health), str(self.current_health), str(self.knocked_out)))
    
    def lose_health(self, health_hit):
        self.current_health = self.current_health - health_hit
        return "{name} got hit and now has {current_health}".format(name=self.name, current_health=self.current_health)
    
    def regain_health(self, health_boost):
        self.current_health = self.current_health + health_boost
        print ("{name} now has {current_health}".format(name=self.name, current_health=self.current_health))
    
    def knock_out(self):
        self.knocked_out = True
    
    def revive_pokemon(self):
        self.knocked_out = False
    
    def add_experience(self):
        self.experience += 1
        
        if self.experience > 9:
            self.level += (self.level * 0.10)
            self.experience = 0
            self.evolve()

    def evolve(self):
        #This superclass method is to be added logic to when creating a class for specific pokemon
        # The child class needs a class varible for possible names when evolving
        if self.level >= self.base_level * 1.20:   
            self.level += self.level * 0.20
            self.base_level = self.level
            # this self.name = possible_names.pop() needs to be added to method as well as the list of possible names
        else:
            pass
        
    def attack(self, attacked_pokemon):
        
        if self.knocked_out:
            return print("Can't attack, pokemon is knocked out")
        
        print("{name} is attacking {attacked_pokemon}".format(name=self.name, attacked_pokemon=attacked_pokemon.name))
        a_p_type = attacked_pokemon.type
        
        advantage = { 'Fire':'Electricity',
                      'Water': 'Fire',
                      'Electricity' : 'Water'
                    }
        
        disadvantage = { 'Electricity':'Fire',
                         'Fire': 'Water',
                         'Water' : 'Electricity'
                       }
        
        if advantage[self.type] == a_p_type:
            attacked_pokemon.lose_health(self.level * 2)
            self.add_experience()
        
        elif disadvantage[self.type] == a_p_type:
            attacked_pokemon.lose_health(self.level / 2)
            self.add_experience()
        
        else:
            attacked_pokemon.lose_health(self.level)
            self.add_experience()
        
        if attacked_pokemon.current_health <= 0:
            print("{attacked_pokemon} is knocked out you have to switch pokemon to continue to fight".format(attacked_pokemon=attacked_pokemon.name))
            attacked_pokemon.knock_out()



class Trainer():
    def __init__(self, name, potions, pokemons):
        self.name = name
        self.potions = potions
        self.pokemons = pokemons[:6]
        self.active_pokemon = 0
        # Possiblt run the switch pokemon method when initializing
        
    def __repr__(self):
        return str(self.name +  str(self.pokemons) + ", " + str(self.active_pokemon) )
        #", " + str(self.potions) + ", " +

    def use_potion(self):
        
        if self.pokemons[self.active_pokemon].knocked_out == True:
            return print('Cannot use potion, pokemon is knocked out')
        
        if self.potions > 0:
            print("{active_pokemon} is being healed".format(active_pokemon= self.pokemons[self.active_pokemon].name))
            self.pokemons[self.active_pokemon].regain_health(self.pokemons[self.active_pokemon].max_health - self.pokemons[self.active_pokemon].current_health )
            self.potions = self.potions - 1
        else:
            print(self.name + " is out of potions")
    
    def switch_pokemon(self):
        
        try:
            for pokemon in [x for x in self.pokemons if  x.knocked_out == False]:
                print (pokemon.name, str(self.pokemons.index(pokemon)))
        except ValueError:
            print('ooos')
         
        new_pokemon = input("pick what pokemon you want to activate: ")
        
        try:
            new_pokemon = int(new_pokemon)
        except ValueError:
            new_pokemon = 7
        
        if new_pokemon in range(len(self.pokemons)):
            self.active_pokemon = new_pokemon
        else:
            print('Not a valid pokemon, pokemon number 0 pick as default')
            question = input("Would you like to pick again? Y/N: ")        
            if question == 'Y':
                self.switch_pokemon()
            else:
                print('You did n not answer Y (yes), pokemon number 0 picked as default')
                self.active_pokemon = self.pokemons[0]
      
    def attack_trainer(self, other_trainer):
        self.pokemons[self.active_pokemon].attack(other_trainer.pokemons[other_trainer.active_pokemon])



""" Different tests """

        
charmander = Pokemon("Charmander", 45, "Fire")

pikachu = Pokemon("Pikachu", 65, "Electricity")

#print(charmander, pikachu)

jessie = Trainer("Jessie", 4, [charmander] )

tom = Trainer("Tom", 4, [pikachu, charmander])

#print(jessie)

#tom.switch_pokemon()

#tom.attack_trainer(jessie)

#print(jessie)

#print(tom)

#print(tom)
print(jessie)
jessie.attack_trainer(tom)
print(tom)
tom.use_potion()
#print(tom)
#print(tom.active_pokemon)
#print(jessie.active_pokemon)
#tom.attack_trainer(jessie)
#tom.switch_pokemon()
#print(jessie)
#tom.attack_trainer(jessie)
#charmander.knocked_out = True
#print(jessie)







