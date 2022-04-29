__author__ = "Nhu Nguyen"


from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 0.5
    EFFECTIVENESS_GRASS = 2

    def __init__(self) -> None:
        PokemonBase.__init__(self, 7, "Fire")

    def get_name(self):
        return "Charmander"

    def get_speed(self):
        return 7 + self.level

    def get_attack(self):
        return 6 + self.level

    def get_defence(self):
        return 7
    
    def damage_after_attacked(self, another_pokemon: PokemonBase)-> None:
        damage = self.attack_calculation(another_pokemon)
        if damage > self.defend:
            self.hp -= damage
        else:
            self.hp -= damage//2 
    
    def __str__(self) -> str:
        return "Charmander's HP = "  + str(self.hp) + " and level = " + str(self.level)



class Bulbasaur(PokemonBase):
    EFFECTIVENESS_FIRE = 2
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 0.5

    def __init__(self) -> None:
        PokemonBase.__init__(self, 9, "Grass")

    def get_name(self):
        return "Bulbasaur"

    def get_speed(self):
        return 7 + self.level // 2

    def get_attack(self):
        return 5

    def get_defence(self):
        return 5

    def damage_after_attacked(self, another_pokemon: PokemonBase) -> None:
        damage = self.attack_calculation(another_pokemon)
        if damage > self.defend:
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def __str__(self) -> str:
        return "Bulbasaur's HP = " + str(self.hp) + " and level = " + str(self.level)



class Squirtle(PokemonBase):
    EFFECTIVENESS_FIRE = 0.5
    EFFECTIVENESS_WATER = 2
    EFFECTIVENESS_GRASS = 1

    def __init__(self) -> None:
        PokemonBase.__init__(self, 8, "Water")

    def get_name(self):
        return "Squirtle"

    def get_speed(self):
        return 7

    def get_attack(self):
        return 4 + self.level // 2

    def get_defence(self):
        return 6 + self.level

    def damage_after_attacked(self, another_pokemon: PokemonBase) -> None:
        damage = self.attack_calculation(another_pokemon)
        if damage > self.defend:
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def __str__(self) -> str:
        return "Squirtle's HP = " + str(self.hp) + " and level = " + str(self.level)

