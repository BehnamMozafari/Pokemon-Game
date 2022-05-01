__author__ = "Nhu Nguyen"

""" Pokemon.py implementation:  

Personalises attributes for Charmander, Bulbasaur, Squirtle class 

"""

from pokemon_base import PokemonBase

"""Charmander class"""


class Charmander(PokemonBase):
    """Charmander type effectiveness"""
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 0.5
    EFFECTIVENESS_GRASS = 2

    def __init__(self) -> None:
        PokemonBase.__init__(self, 7, 1, "fire")
        self.battled = 0

    def get_battled(self):
        return self.battled

    def update_battled(self):
        self.battled = 1

    # Charmander name getter
    def get_name(self):
        return "Charmander"

    # Charmander speed getter
    def get_speed(self):
        return 7 + self.level

    # Charmander attack getter
    def get_attack(self):
        return 6 + self.level

    # Charmander defence getter
    def get_defence(self):
        return 7

    # Charmander calculate damage after attack
    def damage_after_attacked(self, another_pokemon: PokemonBase):
        """ Function calculates damage after attack from the opposing pokemon
        :param self: the pokemon itself (fire type)
        :param another_pokemon: the opposing pokemon of type PokemonBase
        :complexity:
        """
        damage = self.attack_calculation(another_pokemon)
        if damage > self.get_defence():
            self.hp -= damage
        else:
            self.hp -= damage // 2


    # String printing
    def __str__(self) -> str:
        """String statement returns Charmander HP and its level"""
        return "Charmander's HP = " + str(int(self.hp)) + " and level = " + str(self.level)



"""Bulbasaur class"""


class Bulbasaur(PokemonBase):
    """Bulbasaur type effectiveness"""
    EFFECTIVENESS_FIRE = 0.5
    EFFECTIVENESS_WATER = 2
    EFFECTIVENESS_GRASS = 1

    def __init__(self) -> None:
        PokemonBase.__init__(self, 9, 1, "grass")
        self.battled = 0

    def get_battled(self):
        return self.battled

    def update_battled(self):
        self.battled = 1

    # Bulbasaur name getter
    def get_name(self):
        return "Bulbasaur"

    # Bulbasaur speed getter
    def get_speed(self):
        return 7 + self.level // 2

    # Bulbasaur attack getter
    def get_attack(self):
        return 5

    # Bulbasaur defence getter
    def get_defence(self):
        return 5

    # Bulbasaur calculate damage after attack
    def damage_after_attacked(self, another_pokemon: PokemonBase):
        """ Function calculates damage after attack from the opposing pokemon
        :param self: the pokemon itself (grass type)
        :param another_pokemon: the opposing pokemon of type PokemonBase
        :complexity:
        """
        damage = self.attack_calculation(another_pokemon)
        if damage > (self.get_defence() + 5):
            self.hp -= damage
        else:
            self.hp -= damage // 2


    # String printing
    def __str__(self) -> str:
        """String statement returns Bulbasaur HP and its level"""
        return "Bulbasaur's HP = " + str(int(self.hp)) + " and level = " + str(self.level)


"""Squirtle class"""


class Squirtle(PokemonBase):
    """Squirtle type effectiveness"""
    EFFECTIVENESS_FIRE = 2
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 0.5

    def __init__(self) -> None:
        PokemonBase.__init__(self, 8, 1, "water")
        self.battled = 0

    def get_battled(self):
        return self.battled

    def update_battled(self):
        self.battled = 1

    def get_name(self):
        return "Squirtle"

    def get_speed(self):
        return 7

    def get_attack(self):
        return 4 + self.level // 2

    def get_defence(self):
        return 6 + self.level

    def damage_after_attacked(self, another_pokemon: PokemonBase):
        """ Function calculates damage after attack from the opposing pokemon
        :param self: the pokemon itself (water type)
        :param another_pokemon: the opposing pokemon of type PokemonBase
        :complexity:
        """
        damage = self.attack_calculation(another_pokemon)
        if damage > (self.get_defence() * 2):
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def __str__(self) -> str:
        """String statement returns Squirtle HP and its level"""
        return "Squirtle's HP = " + str(int(self.hp)) + " and level = " + str(self.level)
